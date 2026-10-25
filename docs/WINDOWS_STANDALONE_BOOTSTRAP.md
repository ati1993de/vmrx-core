# VMRX Core v0.1.2 — standalone Windows network troubleshooting

**Purpose:** Distinguish the expected short initial state `height 1/1, ISOLATED, 0 peers` from persistent failure to discover any VMRX peer. Neither state means block 1 has been validated until the local chain height grows beyond 1.

## Confirm the current file and run independently

Get the official [VMRX Core v0.1.2 Windows archive](https://github.com/ati1993de/vmrx-core/releases/tag/v0.1.2), verify SHA256SUMS and extract it completely. Open PowerShell in the extracted folder. The binary must be named `vmrxd.exe` and must identify itself as `VMRX Core v0.1.2`.

If VMRX Node & Miner is already open, its daemon may be listening on ports 29780 and 29781. For a completely independent test use **29880** for local P2P and **29881** for local RPC, with a separate data directory. Do not reuse a GUI-owned or production blockchain database:

```powershell
.\vmrxd.exe --version
.\vmrxd.exe --data-dir "$env:LOCALAPPDATA\VMRX-Core-Standalone-Test" --p2p-bind-ip 127.0.0.1 --p2p-bind-port 29880 --rpc-bind-ip 127.0.0.1 --rpc-bind-port 29881 --no-zmq --no-igd --disable-dns-checkpoints --check-updates disabled --log-level 2
```

**Do not add a peer parameter in this first test:** the goal is to verify whether the daemon's built-in VMRX bootstrap candidate list works without GUI intervention. Give the process time to begin P2P connection attempts. In the running daemon console enter `status`, `print_cn` and `sync_info`. A successful outcome has at least one real peer and a local chain height that rises past block 1 toward the network tip.

## If still isolated

Check Windows outbound TCP access to the known VMRX peer from **a second PowerShell window**:

```powershell
Test-NetConnection 31.70.81.5 -Port 29780
```

A successful TCP connection does not prove the remote node is on the correct chain or that block consensus works. Check `print_cn` and the Core log for actual handshake/sync progress.

Stop the standalone process gracefully by typing `exit`, then retry it using the same isolated data directory and options **plus** `--add-priority-node 31.70.81.5:29780`. Unlike `--add-exclusive-node`, a priority node does not disable discovery from other peers. If the explicit priority peer works but the built-in seed path does not, capture both log files before filing a bug.

**Avoid** supplying upstream Monero nodes or copying Monero data directories. Do not expose the unrestricted JSON-RPC service to the internet. The other candidate IP, `217.154.93.20:29780`, has not independently passed a VMRX handshake.

## What is proven

GitHub Actions' v0.1.2 Windows and Linux Core pipelines verified fresh full-node P2P sync to the original mainnet through canonical height 1193, but those tests specified a known peer on the command line. The separate `standalone-bootstrap-windows.yml` workflow tests the **official released Windows ZIP**, verified by SHA-256, with **zero explicit peer overrides** and a clean database; it checks at least one peer and exact historic hashes after syncing. **Two outcomes on 25 October 2026:** one independently tested official Core ZIP boot discovered 2 peers, reached height 1221 and matched all six historical hashes ([passing run](https://github.com/ati1993de/vmrx-core/actions/runs/40185038433)). Another identically configured first boot remained at 0 peers for five minutes despite successful transient seed handshakes ([failing run](https://github.com/ati1993de/vmrx-core/actions/runs/40184857431)). This confirms a **seed discovery reliability issue**, not a block-1 consensus rejection. A proposed [non-consensus persistent bootstrap fix](https://github.com/ati1993de/vmrx-core/pull/3) is under test and not yet released.

The `update` interactive daemon command requires a parameter (for example `update check`), not a bare `update`. That error is unrelated to P2P connection establishment.

VMRX is not a wallet, and no external-funds spend or deterministic founder seed restoration has been independently verified.
