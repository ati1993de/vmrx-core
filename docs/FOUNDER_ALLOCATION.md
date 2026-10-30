# Mandatory 200,000 VMRX founder premine disclosure

**VMRX is NOT premine-free or fair-launch.** The modified RC1/RC2 consensus rules allocate **200,000.000000000000 VMRX at mainnet block 1** to the founder's existing wallet. A normal mining subsidy was additionally created in that block. The operator has stated that this initial allocation is intentional.

The **historical mainnet block-1 coinbase** consists of exactly **200,000.000000000000 VMRX founder allocation + 35.184304979968 VMRX normal mining subsidy = 200,035.184304979968 VMRX total**. The Core explicitly validates the original block and miner-transaction hashes and both outputs before allowing that one-time exception. It cannot be repeated for another block by ordinary mining.

**The starting block subsidy is NOT 0.6 VMRX.** VMRX uses a supply-dependent, decreasing Monero-derived emission curve. For illustration, after the historical founder block, the *unpenalized base subsidy calculated for block 2* is **34.802768144669 VMRX**, assuming the cumulative generated amount defined by the fixed historical block. Block-weight penalties and transaction fees can affect the actual reported coinbase. **0.6 VMRX is the later tail-emission minimum**, not a fixed reward from launch. There is **no fixed maximum supply** because the tail subsidy continues; no scheduled halvings are defined.

For the formula, 12-decimal precision, coinbase maturity (60 blocks), and authoritative code links, see [VMRX emission specification](EMISSION.md).

## Status of tests

- Block-1 founder allocation verified by the RC2 operator script; block hash recorded in release launch manifest.
- Original founder wallet at height 69 reported total `202366.823008319883 VMRX`, unlocked `200313.604591476068 VMRX` on 2026-10-24. This is an operator screenshot/log observation, not proof of spendability.
- A transfer spending a matured founder output and its receipt on a second independently controlled wallet are **not yet verified**.
- A restored wallet produced a *different primary address* in a previous operator test; that seed must **not** be claimed to back up the founder wallet. Verify recovery against the original address offline before public launch.

Always publish the premine, destination governance/distribution policy, and any lock-up before exchange/pool integrations. Do not reuse VMESH's no-premine disclosure for VMRX.
