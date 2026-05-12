# Counsel

> Legal matter command.

[![CI](https://github.com/szl-holdings/counsel/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/szl-holdings/counsel/actions/workflows/ci.yml) [![CodeQL](https://github.com/szl-holdings/counsel/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/szl-holdings/counsel/actions/workflows/codeql.yml) [![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/szl-holdings/counsel/badge)](https://securityscorecards.dev/viewer/?uri=github.com/szl-holdings/counsel)
[![Status](https://img.shields.io/badge/status-alpha-C8B26A?style=flat-square)](#status) [![License](https://img.shields.io/badge/license-Proprietary-1F2937?style=flat-square)](./LICENSE) [![Security policy](https://img.shields.io/badge/security-policy-01696F?style=flat-square&logo=github&logoColor=white)](./SECURITY.md)
[![Runtime](https://img.shields.io/badge/runtime-ouroboros%20v6.2.0-2DA44E?style=flat-square)](https://github.com/szl-holdings/ouroboros) [![Runtime tests](https://img.shields.io/badge/runtime%20tests-218%2F218-2DA44E?style=flat-square)](https://github.com/szl-holdings/ouroboros) [![Thesis](https://img.shields.io/badge/thesis-v11%20published%20%C2%B7%20v12%20in%20review-805AD5?style=flat-square)](https://github.com/szl-holdings/ouroboros-thesis) [![Lean](https://img.shields.io/badge/Lean%204-kernel--verified-2D5BB9?style=flat-square&logo=lean&logoColor=white)](https://github.com/szl-holdings/lutar-lean)

Counsel turns legal exposure into a tracked, governed workflow: matter lifecycle, obligation dependency mapping, AI-assisted review with human gates, and proof-chain delivery for audit and compliance.

## What Counsel does

- **Matter lifecycle tracking** — intake to resolution with stage gates.
- **Obligation graph** — deadlines, dependencies, and cascading impact.
- **Governed document review** — AI proposes, counsel approves, ledger records.
- **Exposure scoring** — quantified risk with explainable rationale.
- **Audit-grade proof chain** — every decision linkable to evidence and approver.

## Architecture

Counsel is a domain surface on the SZL Holdings platform. Every action is routed through the same governed pipeline:

```
sense → structure → correlate → explain → recommend → approve → execute → proof
```

The execution fabric is [**A11oy**](https://github.com/szl-holdings/a11oy). The bounded-loop kernel underneath every domain pack is [**ouroboros**](https://github.com/szl-holdings/ouroboros) — implementing the [Lutar Invariant](https://github.com/szl-holdings/ouroboros-thesis) for measurable convergence with auditable closure.

## Status

**Alpha.** Counsel is under active development as part of the SZL Holdings platform. Public releases are tagged via [GitHub releases](https://github.com/szl-holdings/counsel/releases). Security disclosures: see [SECURITY.md](./SECURITY.md).

## Security & governance

- CI on every push and pull request
- CodeQL static analysis on the default branch and every PR
- OpenSSF Scorecard published weekly, score visible in the badge above
- Dependabot updates, weekly cadence, SHA-pinned actions
- Secret scanning and push protection enabled
- Branch protection: signed commits, required reviews, no force push, no deletion
- Reusable workflows pinned to commit SHAs ([szl-holdings/.github](https://github.com/szl-holdings/.github))

Report a security issue privately via [GitHub Security Advisories](https://github.com/szl-holdings/counsel/security/advisories/new) or [stephen@szlholdings.com](mailto:stephen@szlholdings.com).

## Mechanisms it inherits

The counsel surface inherits the same six machine-verified mechanisms as every other SZL surface:

| # | Mechanism | Where it's proven |
|---|---|---|
| I | Λ-gate (9-axis Lutar Invariant) | [`lutar-lean/Lutar/Invariant.lean`](https://github.com/szl-holdings/lutar-lean/blob/main/Lutar/Invariant.lean) |
| II | Receipt chain (signed bounded recursion) | [`szl-holdings/ouroboros`](https://github.com/szl-holdings/ouroboros) v6.2 substrate |
| III | Bekenstein gate (information-bounded admit) | Paper v11 §3.3 |
| IV | Dual-witness verdict (MATCH/DIVERGE) | Paper v11 §3.4 |
| V | Witness diversity (Gauss class-number gating) | Paper v12 §4 (in review) |
| VI | Reference-vector parity (bit-exact across runtimes) | [`RefVectors.lean`](https://github.com/szl-holdings/lutar-lean/blob/main/RefVectors.lean) |

Verified test counts: ouroboros runtime **218/218**; full platform monorepo **1,220 tests across 76 packages** (incl. MCP gateway 27/27 e2e). Paper line v1–v11 published on Zenodo (concept DOI [10.5281/zenodo.19944926](https://doi.org/10.5281/zenodo.19944926)); v12 in review ([thesis PR #25](https://github.com/szl-holdings/ouroboros-thesis/pull/25)).

## Citation

If you reference Counsel academically or in industry research, use the metadata in [`CITATION.cff`](./CITATION.cff).

## License

Counsel is proprietary. See [LICENSE](./LICENSE) and [NOTICE](./NOTICE). The underlying [ouroboros runtime](https://github.com/szl-holdings/ouroboros) is Apache-2.0 and the [Ouroboros Thesis](https://github.com/szl-holdings/ouroboros-thesis) is CC BY 4.0.

---

**[SZL Holdings](https://szlholdings.com)** · Founder & CEO **Stephen P. Lutar Jr.** · [stephen@szlholdings.com](mailto:stephen@szlholdings.com)

© 2024–2026 SZL Holdings. All rights reserved.
