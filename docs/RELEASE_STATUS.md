# VMRX Core v0.1.0 — Public release scope

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
4. Native Windows Core daemon build, installation, runtime and network tests.
5. Reproducible builds, signing and independent security review.
6. Original Monero build/CI workflows require fork-specific adaptation.

## Release binary provenance

The Linux `v0.1.0` release reuses exactly the same archive bytes as the previous `v0.1.0-rc.2` operator-tested Linux release, with a clearer filename and updated GitHub release metadata. It is **not** rebuilt from the v0.1.0 source commit. The SHA256SUMS released under v0.1.0 matches the new filename.

## Network/distribution disclosure

VMRX has a 200,000 VMRX **founder premine in block 1**, coinbase maturity 60 blocks, Monero-derived RandomX and ongoing 0.6 VMRX tail subsidy. No strict maximum supply. VMRX is not the VMESH PoW blockchain.

`v0.1.0` denotes the first public main-channel distribution, **not** a claim that the project is audited or safe to use for significant assets.
