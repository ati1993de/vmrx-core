# VMRX Core v0.1.3 — Standalone P2P bootstrap reliability fix

VMRX Core v0.1.3 corrects intermittent failure of the standalone daemon to retain a usable mainnet connection during its first synchronization. This is a **non-consensus** maintenance release.

## Fixed

- When started on **VMRX mainnet without manually specified peer flags**, `vmrxd` now maintains the two existing built-in VMRX bootstrap addresses as persistent preferred outbound peers, rather than relying solely on brief seed handshakes that close before a usable P2P connection is established.
- Keeps the ability to discover peers normally after connecting.
- Explicit `--add-priority-node`, `--add-exclusive-node`, `--seed-node`, `--add-peer`, `--offline` and testnet/stagenet usage retain their previous behavior. No upstream Monero peers are used.
- Correctly branded native `vmrxd.exe` for Windows and `vmrxd` for Linux.

## Regression and compatibility

- Mainnet genesis and all historical blockchain consensus rules are **unchanged**. In particular, the historical block 1 containing the disclosed **200,000 VMRX founder premine** remains validated exactly as before.
- Fresh Linux and Windows CI builds validate the actual VMRX P2P mainnet through historical height 1193 and check original chain hashes at heights 0, 1, 2, 10, 100 and 1193.
- The Windows build additionally runs **two independent fresh-data standalone first-boot tests without any manual peer override**, requiring working peer connections and full historical mainnet synchronization.
- The official v0.1.2 standalone binary demonstrated this reliability issue: one clean Windows test synced to height 1221 with 2 peers, but another stayed at 0 peers for five minutes despite successful transient seed handshakes. This is not a reason to regenerate the genesis or relax any consensus validation.
- These are automated functional checks, not a guarantee of perpetual seed uptime or an independent security audit.

## Packages

- `VMRX-Core-windows-x86_64-v0.1.3.zip` — newly compiled Windows x64 native daemon, official VMRX Windows icon and required MinGW runtime libraries.
- `VMRX-Core-linux-x86_64-v0.1.3.tar.gz` — newly compiled Linux x86_64 native daemon.
- `SHA256SUMS` — release archive checksums.

On Windows, extract **all** ZIP contents (not just the EXE) to a new directory and run `vmrxd.exe` as an ordinary user. Keep RPC bound to `127.0.0.1:29781`; P2P is `29780/TCP`. Never share VMRX chain data or wallet data with upstream Monero or VMESH. Safely back up your existing data before replacing a live installation.

**Operator note:** The separately published **VMRX Node & Miner GUI v0.1.2** still contains the exact Core **v0.1.2** archive and explicitly configures a preferred peer. It is not automatically upgraded by this separate Core release. A future GUI bundle can use Core v0.1.3 after separate integration testing.

**Wallet limitation:** This Core daemon is not a verified standalone wallet. Founder mnemonic/seed recovery, wallet spend/receive and independent security assessment remain unresolved. Never enter seeds into the Node & Miner GUI; do not share keys or seed phrases.
