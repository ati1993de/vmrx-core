# VMRX Core v0.1.1 — Windows + Linux public release scope

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
4. **Cross-platform VMRX peer synchronization and independent mainnet consensus validation**. The native Windows daemon now builds and starts successfully, and it returns the exact Linux mainnet genesis via localhost RPC; a full live-network peer-sync test remains open.
5. Reproducible builds, signing and independent security review.
6. Original Monero build/CI workflows require fork-specific adaptation.

## Release binary provenance

**v0.1.1 Windows x64:** the native Core ZIP is byte-for-byte copied from the successful GitHub Actions build on `main` (run `40134713729`, source commit `029c393fb9716bc666c7617f60959e2525a39b9c`). It includes a real MinGW64 Windows `monerod.exe` and DLL dependencies. Windows RPC genesis matched `405baab8805904ffb7d3643a5004c43b45fc3f5f4c97e712ba4c078a384139d4`. This does not certify live-network sync or wallet safety.

**v0.1.1 Linux x86_64:** the archive is **byte-for-byte identical** to Linux `v0.1.0` (SHA256 `399e0c4695127b533c373a29239703a5a369e0e43434a49ddd378b007114147f`). Linux `v0.1.0` itself reused the RC2 tested operator binary; Linux binaries were **not rebuilt** for the new tag. Both v0.1.1 archives have new filename-specific `SHA256SUMS`.

## Network/distribution disclosure

VMRX has a 200,000 VMRX **founder premine in block 1**, coinbase maturity 60 blocks, Monero-derived RandomX and ongoing 0.6 VMRX tail subsidy. No strict maximum supply. VMRX is not the VMESH PoW blockchain.

`v0.1.1` adds an official Windows x64 Full Node distribution alongside Linux and confirms deterministic mainnet genesis via local RPC. It is **not** a claim that the project is audited or safe to use for significant assets.
