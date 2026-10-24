# VMRX Core v0.1.1 — Windows x64 full node + Linux x86_64

**VMRX is an independent, Monero-derived RandomX PoW chain, not Monero or the VMESH SHA-256d network.**

This is the first official Windows Core distribution. The previously published `v0.1.0` contained Linux only. No old release files or existing mainnet blockchain data are changed.

## Download assets

- **Windows x64:** `VMRX-Core-windows-x86_64-v0.1.1.zip` — native MinGW64 Windows `monerod.exe` with runtime DLLs, built from audited-for-genesis VMRX fork source. *Node only; not a wallet or GUI installer.*
- **Linux x86_64:** `VMRX-Core-linux-x86_64-v0.1.1.tar.gz` — **byte-for-byte the same Linux binary archive as v0.1.0**, carried forward intentionally so the already running mainnet is unchanged. This file is *not* claimed as a fresh Linux rebuild.
- `SHA256SUMS` — verifies the exact two distributed archives.

The Windows package is taken from the successful `main` GitHub Actions build **40134713729**, source commit `029c393fb9716bc666c7617f60959e2525a39b9c`. The release workflow checks that this build passed, verifies the downloaded artifact's SHA256SUMS, checks the archive contains `monerod.exe`, and preserves the bytes. The release source/tag contains only publication changes on top of that source revision.

## Verified Windows behavior

- Native Windows x64 executable was compiled from **VMRX Core fork source**; not downloaded or renamed from a Monero binary.
- The Windows daemon was started on localhost, responded to RPC, and returned the exact mainnet genesis `405baab8805904ffb7d3643a5004c43b45fc3f5f4c97e712ba4c078a384139d4`.
- A Linux reference run downloaded the original `v0.1.0` archive, SHA256-verified it, started that daemon, and compared the Genesis TX source bytes and genesis hash.
- **Not yet established:** successful cross-platform synchronization with independently operated mainnet peers, mined-payout spendability, and independent consensus/security audit.

## Windows quick start

1. Download the Windows Core ZIP and `SHA256SUMS`. Verify the ZIP checksum and extract it entirely.
2. Run `monerod.exe` in a regular, unprivileged Windows account using a **dedicated VMRX-only blockchain data directory**. Do not reuse any Monero/VMESH directory.
3. Keep daemon RPC bound to `127.0.0.1:29781`. VMRX P2P uses `29780/TCP`.
4. Allow network sync only to independently verified VMRX peers; `31.70.81.5:29780` was operator-provided, not guaranteed available.
5. Query `http://127.0.0.1:29781/get_info`, then check block 0 and the matching genesis hash before attempting mining.
6. The separate [VMRX Node & Miner GUI](https://github.com/ati1993de/vmrx-node-miner) has a combined Windows GUI + Core package (v0.1.1 workflow verified); use its official release when available.

## Security and economics disclosure

This **is not a completed, audited custody wallet**. The founder-wallet seed restoration and actual external spend/receipt have **not been verified**. The chain has a **200,000 VMRX founder premine at height 1**, a **0.6 VMRX tail emission** and **no fixed maximum supply**. Coinbase maturity is 60 blocks. Do not use significant funds or assume working wallet recovery merely because the daemon starts.

Build logs: https://github.com/ati1993de/vmrx-core/actions/runs/40134713729
Source: https://github.com/ati1993de/vmrx-core
