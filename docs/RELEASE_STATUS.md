# VMRX Core release status — legacy v0.1.0 and current development

## Verified only by operator logs (24 October 2026)

- The VMRX mainnet has separate genesis and P2P/RPC ports.
- Two local nodes accepted the same mined chain tip; a separate VPS synchronized the initial chain over a real network.
- One RandomX CPU thread achieved about 298 H/s; the local test generated blocks that the primary node accepted.
- A founder wallet refreshed through height 69 and displayed an unlocked balance.

These are operator observations, **not independent consensus/security validation**.

## Still unresolved

1. Deterministic founder-seed recovery: the supplied seed restored to a different address.
2. Full transfer/spend plus recipient confirmation across independent nodes.
3. Difficulty adjustment, long-term PoW, difficulty manipulation and emissions audit.
4. **Partially resolved:** native Windows v0.1.2-dev Core compiles, starts, matches Genesis and synchronized at least 201 live mainnet blocks in CI. Full tip sync, installation and long-running Windows P2P remain to be independently verified.
5. Reproducible builds, signing and independent security review.
6. Original Monero build/CI workflows require fork-specific adaptation.

## Release binary provenance

The Linux `v0.1.0` release reuses exactly the same archive bytes as the previous `v0.1.0-rc.2` operator-tested Linux release, with a clearer filename and updated GitHub release metadata. It is **not** rebuilt from the v0.1.0 source commit. The SHA256SUMS released under v0.1.0 matches the new filename.

## Network/distribution disclosure

VMRX has a 200,000 VMRX **founder premine in block 1**, coinbase maturity 60 blocks, Monero-derived RandomX and ongoing 0.6 VMRX tail subsidy. No strict maximum supply. VMRX is not the VMESH PoW blockchain.

`v0.1.0` denotes the first public main-channel distribution, **not** a claim that the project is audited or safe to use for significant assets.


## Status update: native Windows v0.1.2-dev (24 October 2026)

Published Windows **v0.1.1** Core binary is downloadable but an operator observed its sole peer get banned while syncing at genesis height 1. It is not approved as a fully synced production node.

The pending v0.1.2-dev candidate restores strict acceptance of the **single historically documented** VMRX mainnet block-1 founder premine, guarded by the original block hash, miner-tx hash, network/hardfork version, output amounts and subsidy. Windows GitHub Actions confirmed real P2P sync to **height 201 with one peer**, including the historic block-1 reward and hashes. The existing Windrose chain was not reset or altered.

The new build is named `vmrxd.exe`, and GUI changes include truthful zero-peer isolation indication. Candidate peer addresses are `31.70.81.5:29780` (observed VMRX P2P) and `217.154.93.20:29780` (operator-supplied but not protocol-verified).

Both Linux and Windows Core/GUI v0.1.1 archives exist on GitHub. The **Linux Core v0.1.1 archive reused v0.1.0/RC2 bytes** rather than rebuilding from release source. The new Windows v0.1.2-dev must not be tagged until Windows and GUI build/test jobs are green and independent full-tip checks are considered. Founder wallet seed recovery and transfer confirmation remain unresolved.
