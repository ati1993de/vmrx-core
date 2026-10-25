# VMRX Core v0.1.2 — Windows and Linux mainnet compatibility repair

**Security / consensus release:** The public v0.1.1 Windows daemon was able to start at genesis but could not accept mainnet block 1 due to an omitted historic founder-block reward exception. **Do not use v0.1.1 Windows for network synchronization.**

## Verified correction
- Accept **only the historical VMRX mainnet founder block 1** with exact SHA-256 block hash `79030889ec6dd46cf2722defe9523bd38d2379168a27935fa3f1cdfe9397e293`, miner transaction hash `d7f9691cb7c478fd87957e2210df12205399968e394e1d2a3e58ae56fb7b4645`, two original output amounts, proper HF16, known prior subsidy and reward.
- Historical coinbase: **200,000 VMRX founder premine plus 35.184304979968 VMRX block reward**; all other blocks use unchanged reward rules.
- Native **`vmrxd.exe` (Windows x64)**, **`vmrxd` (Linux x86_64)**. The Windows executable contains the official transparent VMRX icon as a PE resource; package includes the ICO and runtime DLL dependencies.
- VMRX-only P2P seeds replace upstream Monero seeds. No Monero blockchain/peer fallbacks.
- Real Windows and fresh native Linux full-node binaries must each sync via genuine VMRX P2P through historical height **1193** and agree with six fixed mainnet block hashes at heights **0, 1, 2, 10, 100, 1193**, before this release is published.
- The operator's isolated Windrose Linux build synchronized to height 1194 and exactly matched the productive chain tip on 2026-10-25. GitHub Actions independently verify newly rebuilt Linux and Windows candidates with separate fresh data directories.

## Downloads
- `VMRX-Core-windows-x86_64-v0.1.2.zip`: full Windows node and required DLLs, `vmrxd.exe` and `vmrx.ico` inside the Core archive.
- `VMRX-Core-linux-x86_64-v0.1.2.tar.gz`: newly compiled Linux daemon, **not** copied from v0.1.0/RC2.
- `SHA256SUMS`: verify archive checksums before extracting.

## Operational safety
Keep RPC on `127.0.0.1:29781`; mainnet P2P uses port `29780/TCP`. Never share the Monero or VMESH chain data directory with VMRX. Backup chain data and wallet data separately before any production upgrade; do not overwrite an operator's live binary or data directory without a maintenance procedure.

VMRX is a separate Monero-derived RandomX blockchain with 200,000 VMRX disclosed founder allocation at historical block 1, a 0.6 VMRX tail reward and no fixed maximum issuance. No independent security audit or end-to-end wallet seed recovery / funds spend verification is claimed. This software is not a wallet; do not send funds to untested addresses. Original Monero project license attribution remains.
