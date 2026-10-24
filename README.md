# VMRX Core · VargaMesh RX

<p align="center"><img src="assets/vmrx-logo.png" alt="VMRX logo" width="144"></p>

**Independent RandomX proof-of-work blockchain · Monero-derived source code**

[Core downloads](https://github.com/ati1993de/vmrx-core/releases/latest) · [Windows / Linux Node & Miner GUI](https://github.com/ati1993de/vmrx-node-miner) · [Security status](docs/RELEASE_STATUS.md)

VMRX is an independent chain with its own genesis, network ID, address prefixes and P2P/RPC ports. It is **not** VargaMesh **VMESH**, the separate SHA-256d/AuxPoW network.

> **Release warning:** This is an initial **public distribution**, not an independently security-audited, production-safe wallet system. Founder seed restoration and actual external spend have not been verified. A native Windows Core binary has not been released. The public Linux v0.1.0 archive reuses the previously tested RC2 binary payload unchanged. Read [verification status](docs/RELEASE_STATUS.md).

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

- [VMRX Core v0.1.0 — Linux x86_64](https://github.com/ati1993de/vmrx-core/releases/latest) — verified distribution archive and SHA256SUMS; derived byte-for-byte from the operator-tested RC2 Linux artifact, *not rebuilt from source for this tag*.
- **Windows Core daemon:** currently **unavailable**. The separate Windows GUI application is only a controller and cannot mine without an independently installed Windows VMRX Core.
- **Wallet:** the forked wallet CLI still displays some upstream Monero strings. No new wallet safety guarantee is made by releasing it.

### Linux node quick start

1. Download Core archive and `SHA256SUMS` from GitHub Releases; check the SHA256 hash before extraction.
2. Extract as an unprivileged user. Keep its VMRX data directory separate from Monero and VMESH databases.
3. Start the bundled `monerod` from the extracted `bin/` folder using mainnet arguments, `--rpc-bind-ip 127.0.0.1 --rpc-bind-port 29781 --p2p-bind-port 29780` and only known VMRX peers.
4. Query local daemon `/get_info`, verify the genesis, then confirm the current chain with independent VMRX nodes. A previously observed VMRX peer is `31.70.81.5:29780`; it is operator-operated and may be unavailable.

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

Several inherited Monero CI workflows do not run correctly for this fork and are archived for later adaptation. A lightweight VMRX metadata and secrets-path workflow now runs on `main` and tags; **it is not a substitute for consensus unit/integration tests or a reproducible build pipeline**.

## License and attribution

VMRX Core derives from Monero. Respect the repository's `LICENSE`, copyright headers and third-party license files. Do not imply an endorsement by upstream contributors. The owner-approved VMRX logo and icons are under `assets/`.
