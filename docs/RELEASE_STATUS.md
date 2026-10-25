# VMRX Core release status — legacy v0.1.0 and current development

## Verified only by operator logs (24 October 2026)

- The VMRX mainnet has separate genesis and P2P/RPC ports.
- Two local nodes accepted the same mined chain tip; a separate VPS synchronized the initial chain over a real network.
- One RandomX CPU thread achieved about 298 H/s; the local test generated blocks that the primary node accepted.
- A founder wallet refreshed through height 69 and displayed an unlocked balance.

These are operator observations, **not independent consensus/security validation**.

## Still unresolved (25 October 2026)

1. Deterministic founder seed recovery: the supplied seed reportedly restored a different address.
2. End-to-end confirmed transfer and recipient spend across independently managed nodes.
3. Comprehensive difficulty adjustment, PoW, emissions, and security audit.
4. **Sustained P2P availability and seed redundancy:** the released v0.1.2 Windows Core independently passed *automatic* standalone seed discovery with no explicit peer override (height 1221, 2 peers, six exact historic hashes). Continued seed reachability over time and global peer diversity are not guaranteed.
5. Reproducible releases, signing, independent external security review and sustained long-running peer availability.
6. Remaining Monero-derived legacy CLI strings and unrelated inherited build pipelines.

**Verified:** The official Core v0.1.2 includes freshly compiled native Windows `vmrxd.exe` and Linux `vmrxd`. GitHub Actions validated both platforms' live synchronization through historical height 1193 with an explicit known VMRX P2P peer and exact canonical hashes of blocks 0, 1, 2, 10, 100 and 1193. Native Windows executable includes the official VMRX icon. Operator screenshots also show the bundled Windows GUI synchronizing with at least one VMRX peer. These observations do not establish independent wallet correctness.

## Release binary provenance

The Linux `v0.1.0` release reuses exactly the same archive bytes as the previous `v0.1.0-rc.2` operator-tested Linux release, with a clearer filename and updated GitHub release metadata. It is **not** rebuilt from the v0.1.0 source commit. The SHA256SUMS released under v0.1.0 matches the new filename.

## Network/distribution disclosure

VMRX has a 200,000 VMRX **founder premine in block 1**, coinbase maturity 60 blocks, Monero-derived RandomX and ongoing 0.6 VMRX tail subsidy. No strict maximum supply. VMRX is not the VMESH PoW blockchain.

`v0.1.0` denotes the first public main-channel distribution, **not** a claim that the project is audited or safe to use for significant assets.


## Release update: VMRX Core v0.1.2 (25 October 2026)

The historic mainnet block-1 coinbase containing **200,000 VMRX founder premine plus the normal block subsidy** is accepted only when the fixed original chain and coinbase identities match. The v0.1.1 Windows Core failed to accept the original block and must not be used for current mainnet syncing; v0.1.2 fixed that incompatibility.

The [official v0.1.2 release](https://github.com/ati1993de/vmrx-core/releases/tag/v0.1.2) contains new native Windows and Linux binaries with SHA256SUMS. Both platforms' tested builds synchronized beyond height 1193 in separate CI clean-data tests, and the Windows executable is branded `vmrxd.exe` with an embedded VMRX logo. [Node & Miner v0.1.2](https://github.com/ati1993de/vmrx-node-miner/releases/tag/v0.1.2) bundles the checksum-verified exact official Windows Core archive and independently checks synchronization beyond historic block 1193.

**Standalone Windows bootstrap verified (25 October 2026):** The [additional CI test](../.github/workflows/standalone-bootstrap-windows.yml) downloaded the **unaltered official v0.1.2 Windows ZIP**, verified SHA-256 and started `vmrxd.exe` with a clean database **without any explicit peer arguments**. It connected to **2 VMRX peers**, synchronized to **height 1221** and checked six historical hashes (heights 0, 1, 2, 10, 100, 1193). The initial operator screenshot showed 0 peers approximately ten seconds after startup: this alone does not establish a defect. [Successful CI run](https://github.com/ati1993de/vmrx-core/actions/runs/40185038433) · [Windows troubleshooting](WINDOWS_STANDALONE_BOOTSTRAP.md).

Founder wallet recovery, external transfer/spendability, and comprehensive independent security review remain unverified.
