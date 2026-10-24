# Native VMRX Core for Windows 10/11 x64

This repository contains the **real, separate VMRX consensus source**, not an upstream Monero executable. Never substitute an official Monero binary: its genesis and network IDs are different.

## Automated Windows build

GitHub Actions workflow: [VMRX Core — native Windows x64 build](../.github/workflows/windows-core.yml)

From a machine authenticated with GitHub CLI:

```bash
gh workflow run windows-core.yml -R ati1993de/vmrx-core --ref main
gh run list -R ati1993de/vmrx-core --workflow windows-core.yml --limit 5
```

This checks out submodules, prepares MSYS2 MinGW64, compiles the C++ VMRX Core, packages its executable and MinGW runtime dependencies, and boots it on Windows. The local RPC genesis test is followed by a live VMRX block-1 peer-sync acceptance test. The RPC smoke test **must return the VMRX genesis**
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

The published v0.1.1 GUI bundle uses `core/monerod.exe`. In the newer v0.1.2-dev candidate, it preselects the VMRX-branded `core/vmrxd.exe`, with legacy support for the old name. The GUI never starts the daemon automatically; users must explicitly start it and select a mining address. This GUI is **not** a wallet and cannot restore seeds, sign or send funds.

## Local manual build

The inherited Monero Makefile includes a `release-static-win64` target and supports MSYS2 MinGW64, but current CI uses `make release-static-win64-daemon -j2`. These are C++ builds requiring CMake, Boost, OpenSSL, ZeroMQ, libsodium, unbound, hidapi and other MSYS2 dependencies. Follow the GitHub Actions file as the versioned setup.

This project is derived from Monero: preserve upstream copyright and license notices. The 200,000 VMRX founder premine is documented in [Founder Allocation](FOUNDER_ALLOCATION.md).


### v0.1.2-dev Windows peer-sync correction

The v0.1.1 release shipped before validation of mainnet block 1, and was observed stuck at height 1 with a blocked Windrose peer. The candidate fixes the historical premine validation and has successfully reached height **201 with 1 P2P peer** on a native Windows Actions runner. Core now builds `vmrxd.exe`, not `monerod.exe`.

Known VMRX mainnet P2P candidates: `31.70.81.5:29780` (operator-validated handshake) and `217.154.93.20:29780` (operator-provided, VMRX P2P handshake still unverified). GUI uses **non-exclusive priority** peers to preserve discovery; do not use Monero peers. RPC 29781 must stay local. For actual release approval, check mainnet tip convergence against Windrose beyond height 201.
