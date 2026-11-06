# StreamShield Security Evolution

An open-source control plane for autonomous, evidence-driven security improvement of StreamShield using Omnara-managed agents and GitHub Actions.

> Status: architecture scaffold. Agent execution adapters, Omnara API integration, isolated staging infrastructure, and merge enforcement must be implemented and validated before autonomous production use.

## Goals

- Run independent defense, authorized red-team, and evaluator agents.
- Discover and use vetted security research and testing tools through a permissioned registry.
- Test only explicitly authorized staging environments with synthetic media and identities.
- Preserve reproducible evidence, shared intelligence, and an auditable history.
- Permit automatic merging only after independent evaluation and mandatory CI/security gates.

## Agent teams

**Defense:** security architect, Django security engineer, streaming/gateway engineer, DRM/playback engineer, defense reviewer.

**Red team:** browser tester, HLS protocol tester, API tester, session/token tester, reconstruction/evidence analyst.

**Independent evaluator:** verifies findings, reproduces fixes, checks regressions and emits a signed/traceable decision. It must not evaluate its own changes.

## Non-negotiable constraints

- Screen recording and external-camera recording by an authorized viewer are accepted exceptions. They are not vulnerabilities or release blockers. Do not build controls intended to defeat OS/device capture.
- This exception does not permit unauthorized API access, playlist/segment retrieval, token replay, cache leakage, session sharing, cross-tenant access, or unauthorized reconstruction.
- No absolute copy-prevention claims.
- No production credentials, customer media, DRM keys, or production database access in agent jobs.
- Persistent centralized video storage remains Telegram-only per the product requirement; do not add R2, S3, or another persistent object store without an explicit decision.
- The LMS remains the authority for identity, enrollment, and payment decisions.
- Fail closed when the evaluator, evidence, required checks, or authorization boundary is unavailable.

## Quick start

1. Read `docs/architecture.md`, `docs/security-policy.md`, and `docs/omnara-integration.md`.
2. Configure repository secrets only after reviewing the threat model. Never expose secrets to forked or untrusted pull-request code.
3. Build a synthetic-only staging environment and validate its isolation before enabling red-team workflows.
4. Implement and test the Omnara adapter; no provider-specific API assumptions are embedded in this scaffold.
5. Keep automatic merge disabled until branch protection, required checks, independent evaluation, and rollback are verified.

## Repository layout

- `agents/` role prompts and capability boundaries.
- `tools/` vetted tool registry and execution policy.
- `security-evolution/` shared threat intelligence, catalogs, decisions, exceptions, and reports.
- `.github/workflows/` scheduled/manual CI entry points.
- `docs/` architecture, integration, and operations guidance.

## License

Apache-2.0. See `LICENSE`.