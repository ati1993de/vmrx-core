# Ubuntu 24.04 operator deployment — RC2

**Do not run `launch`, `go-live` or Genesis bootstrap commands against an existing mainnet.** Never overwrite `/var/lib/vmrx-mainnet` or `/PRIVATE/`.

The initial Windrose operator package was located at:

`/opt/vmrx/VMRX-RC1-200K/RELEASE/vmrx-linux-x86_64-RC2.tar.gz`

Archive had `bin/monerod`, `bin/monero-wallet-cli`, `bin/monero-wallet-rpc`, wrapper commands (`vmrxd`, `vmrx-wallet-cli`, `vmrx-wallet-rpc`), docs and checksums. Archive is **NOT INCLUDED** here. Transfer the real archive separately from the trusted operator server; verify SHA-256 and manifest on receipt.

## Install-time defects observed and mitigated

1. Extracted `bin/` and `monerod` had mode `0700`; non-root systemd user encountered `status=203/EXEC`. Correct ownership/traversal/execute permissions for the actual target.
2. On Ubuntu 24.04.5 the binary needed Boost 1.83 runtime libraries and `libhidapi-libusb0` and `libunbound8`. The operator installed:

```bash
sudo apt-get update
sudo apt-get install -y \
  libboost-chrono1.83.0t64 \
  libboost-filesystem1.83.0 \
  libboost-program-options1.83.0 \
  libboost-thread1.83.0 \
  libboost-serialization1.83.0 \
  libhidapi-libusb0 libunbound8
```

Inspect `ldd path/to/bin/monerod` for missing libraries. Only install from your distro repositories, never rename a different Boost SONAME to fake compatibility.

## Starting a secondary test node

For a **fresh** secondary node on its own VPS (not replacing mainnet): install the real binary under a dedicated non-root account, use an empty data directory, local-only RPC and bind P2P according to your network plan. Start with `--add-exclusive-node <VERIFIED_VMRX_P2P_HOST>:29780`, never any upstream Monero seeds. Confirm the genesis and block-1 hashes, and compare current block height, tip hash and peer status with the mainnet.

Do not run a public RPC listener. Treat `127.0.0.1:29781` as sensitive; the GUI preview uses local RPC only.
