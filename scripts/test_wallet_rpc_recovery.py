#!/usr/bin/env python3
"""VMRX fork-specific deterministic wallet regression check.

Build BOTH daemon and wallet_rpc_server from the SAME Core commit first.
This script must never print a seed, key, RPC password or request body.
It verifies new EMPTY wallet create/close/reopen/recovery identity, NOT historical
founder recovery nor independently settled real fund transfers.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import secrets
import subprocess
import tempfile
import time
import urllib.request
import urllib.error

GENESIS = "405baab8805904ffb7d3643a5004c43b45fc3f5f4c97e712ba4c078a384139d4"


def rpc(url, method, params=None, opener=None, timeout=6):
    payload = {"jsonrpc": "2.0", "id": "test", "method": method, "params": params or {}}
    request = urllib.request.Request(
        url, method="POST",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with (opener or urllib.request.build_opener(urllib.request.ProxyHandler({}))).open(request, timeout=timeout) as response:
            data = json.load(response)
    except urllib.error.HTTPError as exc:
        # Diagnostic must never reveal credentials, seeds, or response bodies.
        auth_scheme = (exc.headers.get('WWW-Authenticate', '').split(' ', 1)[0] or 'none')
        raise RuntimeError(f'RPC {method} HTTP {exc.code}; authentication scheme={auth_scheme}') from None
    if data.get("error"):
        raise RuntimeError(f"RPC {method} rejected: code {data['error'].get('code', '?')}")
    return data.get("result", data)


def wait_ready(fn, proc, limit=45):
    last_error = None
    until = time.monotonic() + limit
    while time.monotonic() < until:
        if proc.poll() is not None:
            raise RuntimeError("Process exited before RPC became available")
        try:
            return fn()
        except (OSError, ValueError, RuntimeError) as exc:
            last_error = str(exc) if isinstance(exc, RuntimeError) else type(exc).__name__
            time.sleep(0.4)
    raise RuntimeError("Local RPC did not become ready: " + str(last_error))


def run(daemon_binary: Path, wallet_binary: Path):
    if not daemon_binary.is_file() or not wallet_binary.is_file():
        raise RuntimeError("Compile native VMRX daemon and wallet RPC first")
    with tempfile.TemporaryDirectory(prefix="vmrx-wallet-test-") as work:
        root = Path(work)
        chain = root / "chain"
        wallets = root / "wallets"
        chain.mkdir()
        wallets.mkdir()
        user = "vmrx-wallet-test"
        password = secrets.token_urlsafe(32)
        daemon_port, wallet_port = 30781, 30782
        daemon_url = f"http://127.0.0.1:{daemon_port}/json_rpc"
        wallet_url = f"http://127.0.0.1:{wallet_port}/json_rpc"
        flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
        daemon = subprocess.Popen([
            str(daemon_binary), "--non-interactive", "--data-dir", str(chain),
            "--p2p-bind-ip", "127.0.0.1", "--p2p-bind-port", "30780",
            "--rpc-bind-ip", "127.0.0.1", "--rpc-bind-port", str(daemon_port),
            "--add-exclusive-node", "127.0.0.1:1",
            "--no-zmq", "--no-igd", "--disable-dns-checkpoints",
            "--check-updates", "disabled",
        ], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL, creationflags=flags)
        wallet = None
        try:
            got = wait_ready(lambda: rpc(daemon_url, "get_block_header_by_height", {"height": 0}), daemon)
            observed = got["block_header"]["hash"]
            if observed != GENESIS:
                raise RuntimeError("Wrong VMRX genesis; refusing wallet regression test")
            wallet = subprocess.Popen([
                str(wallet_binary), "--wallet-dir", str(wallets),
                "--rpc-bind-ip", "127.0.0.1", "--rpc-bind-port", str(wallet_port),
                "--rpc-login", f"{user}:{password}",
                "--daemon-address", f"127.0.0.1:{daemon_port}",
                "--trusted-daemon", "--log-level", "0",
            ], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL, creationflags=flags)
            auth = urllib.request.HTTPPasswordMgrWithDefaultRealm()
            auth.add_password(None, wallet_url, user, password)
            opener = urllib.request.build_opener(
                urllib.request.ProxyHandler({}), urllib.request.HTTPDigestAuthHandler(auth))
            call = lambda method, params=None: rpc(wallet_url, method, params, opener)
            # An unauthenticated request may receive an HTTP 401, before the
            # wallet engine is ready. Only get_version is wallet-independent.
            wait_ready(lambda: call("get_version"), wallet)
            call("create_wallet", {"filename": "test_original",
                                   "password": "test-password-only-no-funds",
                                   "language": "English"})
            address1 = call("get_address", {"account_index": 0})["address"]
            seed = call("query_key", {"key_type": "mnemonic"})["key"]
            view_key = call("query_key", {"key_type": "view_key"})["key"]
            if len(seed.split()) not in (24, 25):
                raise RuntimeError("Wallet seed has unexpected word count")
            call("store")
            call("close_wallet", {"autosave_current": True})
            call("open_wallet", {"filename": "test_original",
                                 "password": "test-password-only-no-funds"})
            opened = call("get_address", {"account_index": 0})["address"]
            if opened != address1:
                raise RuntimeError("Wallet re-open returned different address")
            call("close_wallet", {"autosave_current": True})
            result = call("restore_deterministic_wallet", {
                "filename": "test_restored", "password": "different-test-password",
                "seed": seed, "seed_offset": "", "restore_height": 0,
                "language": "English",
            })
            address2 = result.get("address") or call("get_address", {"account_index": 0})["address"]
            view_key2 = call("query_key", {"key_type": "view_key"})["key"]
            if address1 != address2 or view_key != view_key2:
                raise RuntimeError("CRITICAL: newly generated wallet seed restoration mismatch")
            call("store")
            call("close_wallet", {"autosave_current": True})
            keys = (wallets / "test_original.keys", wallets / "test_restored.keys")
            if not all(p.is_file() and p.stat().st_size > 100 for p in keys):
                raise RuntimeError("Encrypted wallet .keys files were not saved")
            print("PASS: VMRX native wallet RPC produced matching address and view key after genesis-height mnemonic recovery")
            print("PASS: encrypted keys files present, wallet reopened, daemon genesis matched")
            print("LIMITATION: no funded/spend transaction, historic founder recovery, or independent audit tested")
        finally:
            if wallet and wallet.poll() is None:
                wallet.terminate()
                try:
                    wallet.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    wallet.kill()
                    wallet.wait(timeout=10)
            if daemon.poll() is None:
                daemon.terminate()
                try:
                    daemon.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    daemon.kill()
                    daemon.wait(timeout=10)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--daemon", type=Path, required=True)
    parser.add_argument("--wallet-rpc", type=Path, required=True)
    args = parser.parse_args()
    run(args.daemon.resolve(), args.wallet_rpc.resolve())
