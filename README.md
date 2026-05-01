# Counsel — Legal Matter Command

  > Policy-gated human review for legal matters — every recommendation evidence-backed and auditable.

  [![CI](https://github.com/szl-holdings/szl-holdings-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/szl-holdings/szl-holdings-platform/actions/workflows/ci.yml)
  [![TypeScript](https://img.shields.io/badge/TypeScript-5.9-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
  [![License](https://img.shields.io/badge/license-Proprietary-red?style=flat-square)](../../LICENSE.md)

  [Live Demo](https://szlholdings.com) · [Platform Demo Video](https://szlholdings.com/szl-demo-video/) · [Investor Dashboard](https://szlholdings.com/stephen/investor) · [Architecture](../../docs/architecture/architecture.md)

  ![Counsel — Legal Matter Command](https://raw.githubusercontent.com/szl-holdings/szl-holdings-platform/master/.github/assets/screenshots/counsel-hero.jpg)

  ---
  ## What it does

  Counsel is the **legal matter command surface** — a policy-gated human review workflow for matter intake, conflict checking, document review, citation verification, and timeline reconciliation. Built on the same Ouroboros runtime + Codex decision-receipt kernel as the rest of the platform: every recommendation carries its source citations, validator outcomes, and risk tier.

  ## Government alignment

  Counsel inherits the platform's NYSTEC-audited governance posture:

  - **NIST AI RMF**: full coverage across GOVERN / MAP / MEASURE / MANAGE
  - **DoD Responsible AI Tenets**: 4 of 5 covered (Equitable in 30-day roadmap)
  - **GSA RAG source attribution**: every cited authority hashed via Katzilla primary-source feed (CourtListener, Federal Register)
  - **Human approval at R3/R4**: high-consequence legal actions never execute without explicit human confirmation

  ## Run locally

  ```bash
  pnpm install
  pnpm --filter @workspace/api-server dev
  pnpm --filter @workspace/counsel dev
  ```

  **Primary route:** `/counsel/`

  ## Tech stack

  React 19 + Vite 7 + TypeScript (strict) · Express 5 · PostgreSQL 16 / Drizzle ORM · Multi-provider AI · Ouroboros loop runtime (`PRF_SYSTEM_CLAIMS`) · Codex decision receipts
  
  ---

  **SZL Holdings** · [szlholdings.com](https://szlholdings.com) · [inquiries@szlholdings.com](mailto:inquiries@szlholdings.com)

  ---
  ## About this repository

  This is a public showcase of one product in the [SZL Holdings platform](https://github.com/szl-holdings/szl-holdings-platform) monorepo. It mirrors the README from the platform artifact directory; the canonical, version-controlled source — including the React app, tests, and infrastructure — lives in the platform repo.

  All seven products share the same governed substrate:

  - **[`@workspace/ouroboros`](https://github.com/szl-holdings/ouroboros)** — bounded loops with measurable convergence, v6 ecosystem layer, government readiness module (**133/133 tests**)
  - **[`@workspace/codex-kernel`](https://github.com/szl-holdings/szl-holdings-platform/tree/master/packages/codex-kernel)** — decision receipts, validators, replay, trace-hash verification
  - **The Ouroboros Thesis** — [`szl-holdings/ouroboros-thesis`](https://github.com/szl-holdings/ouroboros-thesis) — architectural rationale + v6 operational contract

  Government readiness audit (NYSTEC pre-briefing, 2026-04-30): [`docs/audit/szl-government-readiness.md`](https://github.com/szl-holdings/ouroboros/blob/main/docs/audit/szl-government-readiness.md)

  © 2026 SZL Holdings. All rights reserved.
  