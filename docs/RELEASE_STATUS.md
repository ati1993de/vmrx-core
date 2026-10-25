# VMRX Core release status — v0.1.3 mainnet maintenance release

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
4. **Long-term P2P resilience:** v0.1.3 repaired intermittent first-boot seed discovery. Windows CI validated two independent clean first boots (height 1239 with 1 peer each), but continued availability of public seeds and decentralized peer diversity are not guaranteed.
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

**Standalone Windows bootstrap verified (25 October 2026):** The [additional CI test](../.github/workflows/standalone-bootstrap-windows.yml) downloaded the **unaltered official v0.1.2 Windows ZIP**, verified SHA-256 and started `vmrxd.exe` with a clean database **without any explicit peer arguments**. It connected to **2 VMRX peers**, synchronized to **height 1221** and checked six historical hashes (heights 0, 1, 2, 10, 100, 1193). A second independent [failing first-boot run](https://github.com/ati1993de/vmrx-core/actions/runs/40184857431) stayed at height 1 with 0 peers for five minutes, despite a successful transient handshake to `31.70.81.5:29780` and an unreachable alternate peer. Therefore automatic discovery is **intermittent in official v0.1.2**; a single successful run does not demonstrate reliability. [Successful CI run](https://github.com/ati1993de/vmrx-core/actions/runs/40185038433) · [Windows troubleshooting](WINDOWS_STANDALONE_BOOTSTRAP.md).

Founder wallet recovery, external transfer/spendability, and comprehensive independent security review remain unverified.


## Release update: VMRX Core v0.1.3 (25 October 2026)

**Latest stable Core:** [v0.1.3](https://github.com/ati1993de/vmrx-core/releases/tag/v0.1.3), providing new, SHA256-verified Windows and Linux node archives. The original v0.1.2 installer-less Core could sometimes stay at height 1 with zero peers after a clean first boot, even after successful temporary P2P seed handshakes. Its candidate fix initially failed because it used `command_line::has_arg` on a defaulted vector option. **v0.1.3** uses `command_line::is_arg_defaulted` and establishes persistent priority connections to the existing VMRX seed candidates only when no explicit peer options are given on normal online mainnet starts.

**Release evidence:** [Final Windows Core CI](https://github.com/ati1993de/vmrx-core/actions/runs/40187138005) compiled the genuine v0.1.3 Windows daemon, checked its embedded official Windows icon, matched original block 1 and six historical hashes, synchronized with real VMRX P2P through height 1238, and subsequently passed **two fresh bootstraps with no user-supplied peers**, each reaching height **1239** and one peer. [Final Linux Core CI](https://github.com/ati1993de/vmrx-core/actions/runs/40187138034) passed a fresh build and mainnet-chain validation. [Release publishing workflow](https://github.com/ati1993de/vmrx-core/actions/runs/40188394739) completed successfully with verified archive checksums.

**GUI version caveat:** [Node & Miner v0.1.2](https://github.com/ati1993de/vmrx-node-miner/releases/tag/v0.1.2) still includes the exact v0.1.2 Windows Core. Its GUI configures a preferred peer, so it is not automatically updated or broken by releasing v0.1.3 separately. Rebuild and test the GUI bundle separately before making it claim to contain Core v0.1.3.

This maintenance release changes no genesis, fork rules, historical founder premine, wallet seed format, transaction rules or reward schedule. Founder mnemonic recovery, independently confirmed transfers and external security audit remain unverified.
