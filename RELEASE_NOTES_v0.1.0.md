# VMRX Core v0.1.0 — Linux x86_64 public release

First main-channel release of the VMRX Linux full-node binary archive and public fork source. **The binary archive is byte-for-byte identical to the previously published RC2 archive**, only renamed. No new independent build or security audit is claimed.

## Included

- `VMRX-Core-linux-x86_64-v0.1.0.tar.gz` — Linux x86_64 VMRX Core, same binary bytes as RC2.
- `SHA256SUMS` — SHA256 of the actual archive distributed under this filename.
- Source code, network specification, documentation, license and brand assets in the public repository.

## Mainnet

RandomX, target 120 seconds, P2P 29780, localhost daemon RPC 29781. Genesis: `405baab8805904ffb7d3643a5004c43b45fc3f5f4c97e712ba4c078a384139d4`.

**200,000 VMRX founder premine** at height 1. Monero-derived tail emission 0.6 VMRX per target block, no strict supply cap.

## Limitations

- **Linux Core only. No native Windows Core binary.** The separate Windows GUI does not include a standalone node.
- Seed restoration did not reproduce the known founder address; spend and receipt tests remain unresolved.
- No independent audit, reproducible binary build, release signing, consensus certification or full production wallet guarantee.
- Upstream Monero daemon/CLI strings remain in the fork; do not mix with Monero peer networks or blockchain databases.

See [Release status](docs/RELEASE_STATUS.md), [Founder allocation](docs/FOUNDER_ALLOCATION.md) and [Security](docs/SECURITY.md) for details.
