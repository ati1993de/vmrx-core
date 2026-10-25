#!/usr/bin/env python3
"""Mainnet block acceptance gate for a freshly built VMRX Linux daemon.

Only starts a disposable, unprivileged-by-CI VMRX node. Never accesses any
operator mainnet database; never calls privileged RPC methods or handles keys.
A passing status flag alone is NOT sufficient: verify canonical block hashes.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import tempfile
import time
import urllib.error
import urllib.request

# Independently reported immutable historic hashes from the operator's
# production mainnet. Height 1193 was compared against two synchronized nodes
# on 2026-10-25; if a real reorg happens, review rather than silently updating.
CHECKPOINTS = {
    0: "405baab8805904ffb7d3643a5004c43b45fc3f5f4c97e712ba4c078a384139d4",
    1: "79030889ec6dd46cf2722defe9523bd38d2379168a27935fa3f1cdfe9397e293",
    2: "85089d1458e2e6f81673ae24dfee40651b375091f9b9c200ecca66b53fda8675",
    10: "ca1253c7cd24f355ecc9b7163764205388281ac0a9ee15c4c2f502df7c0adbba",
    100: "ba4662de0e2e4a16618b5a0fd2ae691297fe3f205491ef2e6b0e6112ce3cf85d",
    1193: "47e0b825d24cf99042fcaf31fb721a2b593d2c3b5e902c6f1e8dd063ed75e591",
}
BLOCK1_REWARD = 200035184304979968

def request_json(url: str, body: bytes | None = None) -> dict:
    request = urllib.request.Request(url, data=body)
    if body is not None:
        request.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(request, timeout=4) as response:
        return json.load(response)

def rpc(base: str, method: str, params: dict) -> dict:
    result = request_json(
        base + "/json_rpc",
        json.dumps({"jsonrpc": "2.0", "id": "vmrx-test",
                    "method": method, "params": params}).encode("utf8"))
    if result.get("error"):
        raise RuntimeError(f"{method}: {result['error']}")
    return result["result"]

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--daemon", type=pathlib.Path, required=True)
    parser.add_argument("--peer", default="31.70.81.5:29780")
    parser.add_argument("--seconds", type=int, default=480)
    parser.add_argument("--log", type=pathlib.Path, default=pathlib.Path("buildlogs/linux-live-sync.log"))
    args = parser.parse_args()
    daemon = args.daemon.resolve(strict=True)
    args.log.parent.mkdir(parents=True, exist_ok=True)
    base = "http://127.0.0.1:29891"
    with tempfile.TemporaryDirectory(prefix="vmrx-core-v012-live-") as data:
        cmd = [str(daemon), "--non-interactive",
               "--data-dir", data,
               "--p2p-bind-ip", "127.0.0.1", "--p2p-bind-port", "29890",
               "--rpc-bind-ip", "127.0.0.1", "--rpc-bind-port", "29891",
               "--no-zmq", "--no-igd", "--disable-dns-checkpoints",
               "--check-updates", "disabled",
               "--add-exclusive-node", args.peer,
               "--log-level", "1", "--log-file", str(args.log.absolute())]
        print("Validating VMRX Core against real independent P2P blocks; private ephemeral data directory.", flush=True)
        proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        start = time.monotonic()
        previous = None
        passed = False
        try:
            while time.monotonic() - start < args.seconds:
                if proc.poll() is not None:
                    raise RuntimeError(f"VMRX Core exited before syncing (status={proc.returncode})")
                time.sleep(3)
                try:
                    info = request_json(base + "/get_info")
                except (OSError, ValueError):
                    continue
                height = int(info.get("height") or 0)
                connections = int(info.get("outgoing_connections_count") or 0)
                if height != previous:
                    print(f"VMRX: height={height}, outgoing_peers={connections}, synced={info.get('synchronized')}", flush=True)
                    previous = height
                if height < 1194 or connections < 1 or not info.get("synchronized"):
                    continue
                for at, expected in CHECKPOINTS.items():
                    result = rpc(base, "get_block_header_by_height", {"height": at})
                    header = result["block_header"]
                    actual = header["hash"]
                    if actual != expected:
                        raise RuntimeError(f"Historical VMRX mainnet hash mismatch at height {at}: {actual}, expected {expected}")
                    if at == 1 and int(header["reward"]) != BLOCK1_REWARD:
                        raise RuntimeError(f"Incorrect historical founder block reward: {header['reward']}")
                assert info["height"] >= 1194
                print(f"PASS: freshly built VMRX daemon accepted mainnet blocks 0..{height - 1}; "
                      "all six checkpoint hashes including 1193 and block-1 reward match; "
                      f"peer count={connections}", flush=True)
                passed = True
                break
            if not passed:
                raise RuntimeError("VMRX Core did not sync with real VMRX peer to historical height 1194 before deadline; release blocked")
            return 0
        finally:
            proc.terminate()
            try:
                proc.wait(timeout=12)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait()
            if args.log.exists() and not passed:
                print("=== Last 90 sync log lines ===", flush=True)
                print("\n".join(args.log.read_text(errors="replace").splitlines()[-90:]), flush=True)

if __name__ == "__main__":
    raise SystemExit(main())
