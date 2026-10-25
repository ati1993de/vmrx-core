# VMRX Core · VargaMesh RX

<p align="center"><img src="assets/vmrx-logo.png" alt="VMRX logo" width="144"></p>

**Independent RandomX proof-of-work blockchain · Monero-derived source code**

[Core downloads](https://github.com/ati1993de/vmrx-core/releases/latest) · [Windows / Linux Node & Miner GUI](https://github.com/ati1993de/vmrx-node-miner) · [Security status](docs/RELEASE_STATUS.md)

VMRX is an independent chain with its own genesis, network ID, address prefixes and P2P/RPC ports. It is **not** VargaMesh **VMESH**, the separate SHA-256d/AuxPoW network.

> **Release status (25 October 2026):** The current supported release is **v0.1.2**, with natively rebuilt `vmrxd.exe` (Windows) and `vmrxd` (Linux). Fresh binaries successfully synchronized via real VMRX peers beyond height 1193 in GitHub CI, including all six canonical historical block hashes; the Windows Core also contains the official VMRX icon. **Older Windows v0.1.1 is broken for mainnet synchronization and must not be used.** This is **not** an independently security-audited wallet: founder seed restoration and real-world send/receive remain unverified. The separate official Windows ZIP bootstrap test **passed**: the standalone daemon started with zero manual peer overrides, discovered 2 peers and synchronized through height 1221 while matching six historic hashes. Read [verification status](docs/RELEASE_STATUS.md).

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

- **Latest: [VMRX Core v0.1.2 — Windows and Linux](https://github.com/ati1993de/vmrx-core/releases/tag/v0.1.2)**. Official files: `VMRX-Core-windows-x86_64-v0.1.2.zip`, `VMRX-Core-linux-x86_64-v0.1.2.tar.gz`, and `SHA256SUMS`. SHA-256 verification is strongly recommended.
- **Windows:** Extract the entire ZIP, preserving `vmrxd.exe`, `vmrx.ico` and accompanying DLLs. Start `vmrxd.exe` from the extracted folder; the first run creates a new blockchain database under the VMRX data directory. **Do not use v0.1.1** for P2P sync.
- **Linux:** Extract the archive to a fresh folder and run `./vmrxd --rpc-bind-ip 127.0.0.1 --rpc-bind-port 29781` using an unprivileged account. The included Linux daemon is newly built from VMRX Core v0.1.2 source.
- **GUI:** [VMRX Node & Miner v0.1.2](https://github.com/ati1993de/vmrx-node-miner/releases/tag/v0.1.2) bundles the **exact checksum-verified official Windows Core v0.1.2** and launches it only on user request. The Linux GUI requires separate Linux Core installation.

### Mainnet peer discovery and diagnostics

The standalone Core embeds two VMRX-only bootstrap candidates, `31.70.81.5:29780` (operator-confirmed VMRX seed) and `217.154.93.20:29780` (operator-supplied; not independently protocol-verified). It does **not** use upstream Monero seeds. A newly started `vmrxd` can initially show `height 1/1; network tip unknown; ISOLATED - 0 peers`; this means **no network sync**, not a chain failure by itself. Give the daemon time to connect and request blocks, then use the console commands `status`, `print_cn`, `print_pl` and `sync_info` to inspect the peer state.

If zero peers persist, first ensure outbound TCP access to port 29780. Then restart the Core with an explicit preferred **VMRX** peer such as `--add-priority-node 31.70.81.5:29780` (not exclusive) and inspect its log file. The GUI uses preferred peers, so GUI synchronization alone would not have established default standalone discovery; the independent Windows release-only test has now **verified that separate bootstrap path**. See [Standalone Windows bootstrap diagnostics](docs/WINDOWS_STANDALONE_BOOTSTRAP.md).

Avoid running two local daemons on the same machine using the same RPC (29781) or P2P (29780) listening ports. Their data directories must also be separate. Never reuse upstream Monero or VMESH blockchain databases or wallet keys. Expose RPC on loopback only; restrict firewalls to trusted inbound P2P. The Core daemon is not a complete wallet.

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

Several inherited Monero CI workflows do not run correctly for this fork and are archived for later adaptation. Native VMRX Windows and Linux release pipelines now compile and validate actual mainnet block synchronization through historical height 1193. A separate Windows Core release-only smoke test checks fresh standalone seed discovery. These are functional tests, **not** substitutes for deterministic wallet recovery, end-to-end spend tests, independent consensus audit or reproducible-build verification.

## License and attribution

VMRX Core derives from Monero. Respect the repository's `LICENSE`, copyright headers and third-party license files. Do not imply an endorsement by upstream contributors. The owner-approved VMRX logo and icons are under `assets/`.
