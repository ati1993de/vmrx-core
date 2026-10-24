# VMRX Core — VargaMesh RX

> **Release candidate documentation only.** The real modified consensus source and build provenance must be included and audited before this document can front a public GitHub Core repository.

VMRX is an independent **RandomX proof-of-work** cryptocurrency derived from Monero v0.18.5.4. It has a distinct genesis, network identity, address prefixes and P2P/RPC ports. **VMRX is not VMESH**: VMESH is a separate SHA-256d/AuxPoW network.

## Quick facts

| Setting | VMRX mainnet (operator-tested RC2) |
| --- | --- |
| Algorithm | RandomX (HF16 in RC source) |
| Block interval target | 120 seconds |
| Mainnet P2P | 29780/TCP |
| Mainnet RPC | 29781/TCP — **localhost only** |
| Testnet P2P / RPC | 39780 / 39781 |
| Stagenet P2P / RPC | 49780 / 49781 |
| Mainnet genesis hash | `405baab8805904ffb7d3643a5004c43b45fc3f5f4c97e712ba4c078a384139d4` |
| Initial founder allocation | **200,000 VMRX at block 1 — premine, publicly disclosed** |
| Founder Coinbase maturity | 60 confirmations according to current RC docs; independently test spendability |
| Emission | Monero-derived formula with 0.6 VMRX tail emission per block |
| Fixed maximum supply | **NONE** (tail emission) |
| Code ancestry | Monero v0.18.5.4; upstream attribution and license must be retained |

## Node software

This repository must contain the *real reviewed fork*, not an upstream Monero binary with changed port numbers. Before installation, independently check the genesis, network ID, mining rules, release manifest, SHA-256 sums, and signed tags.

For the tested Linux RC2 package, see [Operator Deployment](docs/OPERATOR_DEPLOY.md). For security status see [Security](docs/SECURITY.md).

## Wallets

`vmrx-wallet-cli` is presently a wrapper around a Monero-derived wallet CLI, and some upstream text may remain. Seed recovery **must reproduce the exact known primary address**; a successfully synced wallet with an unexpected address is not the founder wallet. Never share your seed or wallet password. The wallet and node GUI are separate projects; the first GUI preview contains **no signing or seed input**.

## Mining

On a synchronized local VMRX daemon, `/start_mining`, `/mining_status`, `/stop_mining` expose CPU RandomX mining. Mining to an address is only valid if the VMRX daemon accepts it; wallet balances do not prove the ability to spend without a successful spend test. The RC2 miner was locally tested at 298 H/s on one CPU thread on 2026-10-24.

## Related projects

- `vmrx-node-miner`: standalone GUI preview for local node management and mining.
- Existing separate VMESH Core: https://github.com/ati1993de/vargamesh-core (different chain).

## License & ancestry

Keep the **full existing upstream Monero LICENSE and copyright statements** from the actual fork. Do not remove notices when rebranding `monerod` or wallet binaries. Verify all third-party component licenses before packaging GUI or binaries.

## Read before publishing

- [Consensus and network facts](docs/NETWORK.md)
- [Premine disclosure](docs/FOUNDER_ALLOCATION.md)
- [Security and outstanding work](docs/SECURITY.md)
- [Ubuntu deployment and known installer problems](docs/OPERATOR_DEPLOY.md)
- [Release gating checklist](docs/RELEASE_CHECKLIST.md)
- [RC2 draft release notes](RELEASE_NOTES_RC2.md)
