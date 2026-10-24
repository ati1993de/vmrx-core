# Native VMRX Core for Windows 10/11 x64

This repository contains the **real, separate VMRX consensus source**, not an upstream Monero executable. Never substitute an official Monero binary: its genesis and network IDs are different.

## Automated Windows build

GitHub Actions workflow: [VMRX Core — native Windows x64 build](../.github/workflows/windows-core.yml)

From a machine authenticated with GitHub CLI:

```bash
gh workflow run windows-core.yml -R ati1993de/vmrx-core --ref main
gh run list -R ati1993de/vmrx-core --workflow windows-core.yml --limit 5
```

This checks out submodules, prepares MSYS2 MinGW64, compiles the C++ VMRX Core, packages its executable and MinGW runtime dependencies, and boots it on Windows. The local RPC smoke test **must return the VMRX genesis**
`405baab8805904ffb7d3643a5004c43b45fc3f5f4c97e712ba4c078a384139d4`.

If successful, download the Actions artifact **vmrx-windows-core-buildtest**. The archive is named `VMRX-Core-windows-x86_64-buildtest.zip`, along with SHA256SUMS.

**Buildtest is not a publicly approved mainnet binary.** Before releasing it, check:
- Native Windows process launches outside MSYS2 and its DLLs are included.
- New Windows node synchronized against a genuine VMRX-only peer and reports the same block hashes as an independently running Linux node. A Genesis-only smoke test is not enough.
- Windows wallet opens, refreshes and can restore the expected address **without leaking seeds**; no actual keys in CI logs.
- P2P and RPC are not exposed outside localhost by the GUI default.
- Mainnet compatibility of release source and existing operator-tested Linux RC2 binary is confirmed; the published Linux v0.1.0 archive was not rebuilt from source.
- Separate seed-backup recovery and a small actual incoming/outgoing transaction have been verified.

Only after these pass should the operator upload the tested Windows Core ZIP and a checksum to a GitHub release. Do not alter published Linux files or re-label RC2 as a new Windows build.

## Complete Windows desktop bundle

The separate [VMRX Node & Miner GUI](https://github.com/ati1993de/vmrx-node-miner) includes a `package-full-windows.yml` workflow. It downloads the **approved** Windows Core ZIP and the Windows GUI ZIP from releases, verifies the SHA256 checksums and the packaged node's genesis, and produces a single bundle with:

```text
VMRX-Node-Miner.exe
core/
  monerod.exe
  <required MinGW runtime DLLs>
README-WINDOWS.txt
```

In that bundle the GUI preselects `core/monerod.exe` when launched. The GUI never starts the daemon automatically; users must explicitly start it and select a mining address. This GUI is **not** a wallet and cannot restore seeds, sign or send funds.

## Local manual build

The inherited Monero Makefile includes a `release-static-win64` target and supports MSYS2 MinGW64, but current CI uses `make release-static -j2`. These are C++ builds requiring CMake, Boost, OpenSSL, ZeroMQ, libsodium, unbound, hidapi and other MSYS2 dependencies. Follow the GitHub Actions file as the versioned setup.

This project is derived from Monero: preserve upstream copyright and license notices. The 200,000 VMRX founder premine is documented in [Founder Allocation](FOUNDER_ALLOCATION.md).
