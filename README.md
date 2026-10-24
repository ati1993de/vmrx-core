# VMRX Core · VargaMesh RX

<p align="center"><img src="assets/vmrx-logo.png" alt="VMRX logo" width="144"></p>

**Independent RandomX proof-of-work blockchain · Monero-derived source code**

[Core downloads](https://github.com/ati1993de/vmrx-core/releases/latest) · [Windows / Linux Node & Miner GUI](https://github.com/ati1993de/vmrx-node-miner) · [Security status](docs/RELEASE_STATUS.md)

VMRX is an independent chain with its own genesis, network ID, address prefixes and P2P/RPC ports. It is **not** VargaMesh **VMESH**, the separate SHA-256d/AuxPoW network.

> **Release warning:** **VMRX Core v0.1.1 is now available for Windows x64 and Linux x86_64.** The Windows daemon successfully passed a native build and localhost genesis RPC smoke test; full independent mainnet-peer synchronization and wallet spend/seed recovery remain unverified. This is **not** an independently security-audited, production-safe wallet system. The Linux v0.1.1 archive is byte-for-byte the same binary as v0.1.0. Read [verification status](docs/RELEASE_STATUS.md).

## Mainnet parameters

| Parameter | Setting |
| --- | --- |
| Coin | VargaMesh RX / VMRX |
| Proof of work | RandomX; Monero-derived hard fork 16 configuration |
| Block target | 120 seconds |
| P2P | 29780/TCP |
| Daemon RPC | 29781/TCP (restrict to localhost) |
| Genesis hash | `405baab8805904ffb7d3643a5004c43b45fc3f5f4c97e712ba4c078a384139d4` |
| Historic block 1 | `79030889ec6dd46cf2722defe9523bd38d2379168a27935fa3f1cdfe9397e293` |
| Founder allocation | **200,000 VMRX in block 1 (PREMINE)** |
| Maturity for coinbase | 60 blocks, according to current fork settings |
| Tail emission | 0.6 VMRX / target block |
| Fixed maximum supply | **None** because of tail emission |
| Code origin | Monero 0.18.5.4 fork with upstream notices retained |

### Transparent premine disclosure

The first block distributed **200,000 VMRX to the founder**. It is not a zero-premine fair launch. See [Founder Allocation](docs/FOUNDER_ALLOCATION.md). Tail emission means there is no fixed supply cap.

## Installation / releases

- [VMRX Core v0.1.1 — Windows x64](https://github.com/ati1993de/vmrx-core/releases/download/v0.1.1/VMRX-Core-windows-x86_64-v0.1.1.zip) — native Windows `monerod.exe` plus runtime DLLs, built from the real VMRX fork and verified against the existing mainnet genesis by RPC.
- [VMRX Core v0.1.1 — Linux x86_64](https://github.com/ati1993de/vmrx-core/releases/download/v0.1.1/VMRX-Core-linux-x86_64-v0.1.1.tar.gz) — unchanged binary bytes from tested Linux v0.1.0, not a new Linux build.
- [Release notes and SHA256SUMS](https://github.com/ati1993de/vmrx-core/releases/tag/v0.1.1) — verify all downloads before execution.
- **Windows and Linux Core are full-node daemons, not GUI wallets or key/seed managers.** The separate [VMRX Node & Miner GUI](https://github.com/ati1993de/vmrx-node-miner) controls the local daemon; use its integrated Windows GUI package instead of the standalone Core package if you prefer a graphical interface.

### Node quick start (Windows and Linux)

1. Download the appropriate v0.1.1 Core archive and `SHA256SUMS` from GitHub Releases; verify its SHA256 before extraction.
2. Extract all files as an unprivileged user. **Do not run from inside the ZIP.** Keep the VMRX data directory separate from Monero and VMESH blockchain databases.
3. On Windows, run the extracted `monerod.exe`; on Linux, run `bin/monerod`. Bind RPC locally (`--rpc-bind-ip 127.0.0.1 --rpc-bind-port 29781`) and use VMRX P2P port `29780` with independently checked peers.
4. Query `/get_info`, verify the genesis `405baab8805904ffb7d3643a5004c43b45fc3f5f4c97e712ba4c078a384139d4`, then verify block height/tip against independent mainnet nodes. Previously observed peer `31.70.81.5:29780` is operator-run and may be unavailable.

More details: [Operator deployment](docs/OPERATOR_DEPLOY.md). **Do not expose unrestricted RPC publicly.** The inherited Monero daemon binary name does not make the fork interchangeable with Monero network data or peers.

## Mining

CPU mining is available through local RPC methods `/start_mining`, `/mining_status` and `/stop_mining`. One-thread operator testing measured **298 H/s** and locally accepted blocks on 24 October 2026. This does **not** establish independent consensus validation or reward spendability. Only mine to an address you can independently recover.

## Wallet caveat

One existing founder wallet displayed `200313.604591476068 VMRX` unlocked when synced to reported height 69. However, a restoration attempt from an available seed produced a **different, empty wallet address**. Independent founder seed restoration and a successful spend/receipt remain open issues. Do not disclose seeds or wallet files.

## Code & project documentation

- [Network specification](docs/NETWORK.md)
- [Founder allocation](docs/FOUNDER_ALLOCATION.md)
- [Security](docs/SECURITY.md)
- [Release readiness and known gaps](docs/RELEASE_STATUS.md)
- [Operator deployment](docs/OPERATOR_DEPLOY.md)
- [VMRX Node & Miner GUI](https://github.com/ati1993de/vmrx-node-miner)

### CI note

The native Windows CI workflow compiles a VMRX-fork `monerod.exe`, launches it on localhost and asserts that its genesis hash matches the published Linux mainnet reference. The v0.1.1 release workflow preserves the CI-verified Windows archive and SHA256-verifies the byte-identical Linux v0.1.0 archive. **This is not proof of reproducible builds, full cross-platform P2P synchronization, independent consensus audit or wallet spendability.**

## License and attribution

VMRX Core derives from Monero. Respect the repository's `LICENSE`, copyright headers and third-party license files. Do not imply an endorsement by upstream contributors. The owner-approved VMRX logo and icons are under `assets/`.
