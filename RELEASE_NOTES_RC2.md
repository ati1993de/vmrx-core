# VMRX Core RC2 — DRAFT release notes

**Status:** operator-tested Linux release candidate, **not independently audited**.  
**Assessment date:** 2026-10-24  
**Do not tag as stable or advertise as fully approved for exchange/listing custody use.**

## RC2 technical capabilities (operator-validated)

- Separate VMRX chain identity and Genesis; local production node started successfully.
- RandomX/HF16 mining works; 298 H/s measured on 1 CPU thread.
- Local P2P block transfer and cross-VPS chain sync to height 5 verified.
- Local mined blocks through height 68 accepted; local peers agreed at height 69.
- Founder output configured for 200,000 VMRX at block 1 (premine).
- Original wallet displayed unlocked balance after refresh to 69/69.

## Important compatibility requirements

- Provided RC2 binary reported upstream Monero-derived version string `v0.18.5.4-release`.
- Linux binary tested on Ubuntu 24.04; depends on Boost 1.83 and other system libraries.
- Archive execute permissions require repair for non-root installations.
- Windows daemon executable / wallet binary and Linux package integrations have not been supplied or tested in this kit.

## Known issues / security

- Independent security and monetary audits **not done**.
- Founder-wallet offline seed backup **not verified against primary address**; attempted restore yielded a different address.
- Confirmed mature-founder output spend still outstanding.
- Default first seed-node configuration remains partially isolated; additional public discovery needs validation.
- Windows/macOS GUI and production-grade wallet UX are still under development.
- **Do not state fixed max supply**: current RC2 has a 0.6 VMRX tail emission.

## Acknowledgements & licensing

VMRX is derived from Monero. Preserve upstream copyrights, license text, and notices from the actual fork's sources. Do not replace them with this README.
