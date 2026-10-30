# VMRX network facts — RC2 / 2026-10-24

Values in this file were extracted from the operator's VMRX source snippets and console outputs. They are not a substitute for reviewing a tagged source tree.

| Network | P2P | RPC | ZMQ configured in source | Address prefix in source | Genesis nonce |
| --- | ---: | ---: | ---: | ---: | ---: |
| Mainnet | 29780 | 29781 | 29782 | 81 | 22093001 |
| Testnet | 39780 | 39781 | 39782 | 181 | 22093002 |
| Stagenet | 49780 | 49781 | 49782 | 191 | 22093003 |

Mainnet block interval target: **120 s**. Algorithm: **RandomX**, HF16. Consensus genesis hash: `405baab8805904ffb7d3643a5004c43b45fc3f5f4c97e712ba4c078a384139d4`. RC2 public mainnet block-1 hash: `79030889ec6dd46cf2722defe9523bd38d2379168a27935fa3f1cdfe9397e293`.

## Mining and monetary parameters (consensus source)

- Normal block subsidy: **supply-dependent and decreasing**, initially around **35 VMRX**, rather than 0.6 VMRX from launch.
- Historic mainnet block 1: **35.184304979968 VMRX** regular subsidy plus **200,000 VMRX** one-time founder premine; total coinbase **200,035.184304979968 VMRX**.
- Tail emission: **0.6 VMRX per 120-second target block**, only after the declining base subsidy reaches the tail floor.
- Supply: **no fixed maximum**; **no scheduled Bitcoin-style halvings**.
- Monetary precision: **12 decimals**; miner coinbase maturity: **60 blocks**.
- Reference: [VMRX emission calculation and source verification](EMISSION.md).

## Operator-observed test outcomes

- First RC2 production node on Windrose had 0 outgoing connections owing to intentionally isolated `--add-exclusive-node 127.0.0.1:1`; inbound P2P remained functional.
- Local second node accepted and synchronized blocks 1–4.
- Separate Ubuntu VPS connected to the operator's Windrose P2P address and synchronized to height 5 on 2026-10-24.
- After CPU mining on a local test node, two Windrose daemons agreed at height 69. **Confirm cross-VPS sync at 69 independently**.

## Secure networking

- RPC: `127.0.0.1:29781` only; never expose unrestricted daemon RPC to the Internet.
- Public mainnet P2P: TCP `29780`; validate inbound access with a different host and review firewall rules.
- Never configure Monero seed nodes or Monero peer lists on this separate network.
- Only use peer addresses confirmed to be serving matching VMRX genesis and consensus data.
- Do not confuse a node's `synchronized: true` with an independently audited consensus implementation.


## VMRX bootstrap candidate nodes (2026-10-24)

- `31.70.81.5:29780` — Windrose mainnet node; a Windows VMRX client has successfully handshaked and received a height announcement, but rejected subsequent block sync because of the historic block-1 premine consensus discrepancy.
- `217.154.93.20:29780` — second operator-provided candidate. P2P daemon presence and VMRX network/chain compatibility are **not yet independently checked**; do not count it as a verified seed until a real handshake and matching block hashes succeed.

These are **VMRX-only P2P port 29780**, not VMESH P2P port 29666, and never Monero peer addresses. Both candidates are attempted non-exclusively on mainnet; third-party peers must still pass real chain identification, PoW and block validation. Restrict daemon RPC 29781 to localhost, and do not reset existing Windrose blockchain state when upgrading.
