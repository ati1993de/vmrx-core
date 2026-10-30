# VMRX Core — mining rewards, emission and historical premine

**Status:** code-based consensus documentation for the current `main` branch (reviewed 2026-10-30). VMRX is an independent Monero-derived RandomX chain; it is **not** SHA-256d/AuxPoW VargaMesh (VMESH).

## Verified network and monetary parameters

| Parameter | Value | Source |
| --- | --- | --- |
| Target time | 120 seconds | [`DIFFICULTY_TARGET_V2`](../src/cryptonote_config.h) |
| Monetary unit | 12 decimals; 1 VMRX = 1,000,000,000,000 atomic units | [`COIN`](../src/cryptonote_config.h) |
| Emission base | `MONEY_SUPPLY = UINT64_MAX`; `EMISSION_SPEED_FACTOR_PER_MINUTE = 20` | [Constants](../src/cryptonote_config.h) |
| Emission shift at 120 seconds | `20 - (2 - 1) = 19` bits | [Reward function](../src/cryptonote_basic/cryptonote_basic_impl.cpp) |
| Normal subsidy | Declines as already-generated coins increase | [Reward function](../src/cryptonote_basic/cryptonote_basic_impl.cpp) |
| Tail floor | `0.3 VMRX per target minute × 2 = 0.6 VMRX` per target block | [`FINAL_SUBSIDY_PER_MINUTE`](../src/cryptonote_config.h) |
| Reward halvings | No scheduled halving interval | [Emission function](../src/cryptonote_basic/cryptonote_basic_impl.cpp) |
| Fixed maximum supply | None: emission continues in the tail phase | [Constants and reward function](../src/cryptonote_config.h) |
| Coinbase maturity | 60 blocks | [`CRYPTONOTE_MINED_MONEY_UNLOCK_WINDOW`](../src/cryptonote_config.h) |
| Historical founder allocation | Exactly 200,000 VMRX, **once at mainnet block 1**, in addition to regular subsidy | [Exact-block exception](../src/cryptonote_core/blockchain.cpp) |

## Consensus reward formula

At major version 16 and the 120-second target, the base reward for a normal block of no more than the reward-penalty weight threshold is:

```text
normal_base_reward_atomic =
    max(((2^64 - 1) - already_generated_coins) >> 19,
        600000000000)

normal_base_reward_vmxr = normal_base_reward_atomic / 1000000000000
```

The last variable name here refers to **VMRX**, not VMESH. The `already_generated_coins` quantity is maintained by the blockchain using the cumulative base reward, including the historical founder block's additional allocation. At excessive block weights the Core can reduce the base reward; transaction fees are added to the miner transaction, so **coinbase total is not always identical to the base subsidy**.

## Historical block examples

| Height | Ordinary unpenalized base subsidy | Exceptional allocation | Combined coinbase / note |
| --- | ---: | ---: | --- |
| 0 (genesis) | 35.184372088831 VMRX (calculation reference) | — | Genesis is not an ordinary publicly mined reward |
| 1 | **35.184304979968 VMRX** | **200,000 VMRX founder allocation** | **200,035.184304979968 VMRX** (exact historical coinbase) |
| 2 | **34.802768144669 VMRX** (formula example) | None | Theoretical subsidy after premine; not a live header query |

Block 1 is constrained to the exact mainnet block hash `79030889ec6dd46cf2722defe9523bd38d2379168a27935fa3f1cdfe9397e293`, coinbase hash `d7f9691cb7c478fd87957e2210df12205399968e394e1d2a3e58ae56fb7b4645`, and the two original output amounts. No arbitrary future block can claim the 200,000 VMRX exception.

The historical combined block-1 amount is also checked by [`scripts/validate_mainnet_sync.py`](../scripts/validate_mainnet_sync.py).

## Verify real block rewards using your own node

Query local daemon RPC only, after synchronizing to the correct VMRX network:

```bash
curl -fsS -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":"0","method":"get_block_header_by_height","params":{"height":1}}' \
  http://127.0.0.1:29781/json_rpc
```

In a successful Monero-compatible RPC response, `result.block_header.reward` is in atomic units. Divide by `10^12` for VMRX. Height 1 should show `200035184304979968` atomic units. If a node is unsynchronized or uses an incompatible fork, do not trust its balance, reward or network status.

**Important:** This documents the implementation, not an independent monetary or security audit. Wallet seed recovery and independently validated spending are not guaranteed by the reward tests. Refer to [release status](RELEASE_STATUS.md) and [founder allocation](FOUNDER_ALLOCATION.md).
