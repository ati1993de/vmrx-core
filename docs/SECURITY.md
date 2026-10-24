# Security and release scope

**Do not consider VMRX audited or exchange-ready solely from the present local tests.**

Known incomplete acceptance gates as of 2026-10-24:

- Independent consensus, cryptographic, money-supply and fork-choice audits.
- Byte-for-byte provenance: signed source tag, reproducible builds and source-to-binary correspondence.
- Independent fork/reorg testing on the exact public RC2 settings.
- Successful spend of matured founder output; repeatable recovery of the **original** founder address using the correct secret backup.
- Cross-VPS relay of **newly mined** blocks and long-running seed-node monitoring.
- Explicit networking safeguards against connecting to Monero's real network.
- Full rebranding and inherited license/copyright audit.
- Windows core builds, installer notarization/signing, Windows AV/SmartScreen reputation, Linux packaging permissions/dependency checks.
- Economic analysis: observed early block production was much faster than target; independently inspect difficulty adjustment with timestamps.

Never upload `/PRIVATE/`, wallets, `.keys`, `.password`, seeds, chain DBs or operator authentication files to GitHub or release archives.

**Desktop GUI preview:** connects only to `127.0.0.1`; no wallet credentials; only spawns an explicitly selected executable. An attached daemon may run shared mining jobs; stop-mining must be used carefully. Test on disposable accounts before mainnet production.
