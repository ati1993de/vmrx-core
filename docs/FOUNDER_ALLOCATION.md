# Mandatory 200,000 VMRX founder premine disclosure

**VMRX is NOT premine-free or fair-launch.** The modified RC1/RC2 consensus rules allocate **200,000.000000000000 VMRX at mainnet block 1** to the founder's existing wallet. A normal mining subsidy was additionally created in that block. The operator has stated that this initial allocation is intentional.

The current software derives an additional mining subsidy under Monero-style emission rules and provides a **0.6 VMRX tail reward per block** in the tail phase. There is **no strict fixed maximum supply**.

## Status of tests

- Block-1 founder allocation verified by the RC2 operator script; block hash recorded in release launch manifest.
- Original founder wallet at height 69 reported total `202366.823008319883 VMRX`, unlocked `200313.604591476068 VMRX` on 2026-10-24. This is an operator screenshot/log observation, not proof of spendability.
- A transfer spending a matured founder output and its receipt on a second independently controlled wallet are **not yet verified**.
- A restored wallet produced a *different primary address* in a previous operator test; that seed must **not** be claimed to back up the founder wallet. Verify recovery against the original address offline before public launch.

Always publish the premine, destination governance/distribution policy, and any lock-up before exchange/pool integrations. Do not reuse VMESH's no-premine disclosure for VMRX.
