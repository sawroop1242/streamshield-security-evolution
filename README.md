# StreamShield Security Evolution

An open-source control plane for autonomous, evidence-driven security improvement of StreamShield, using Omnara-managed agents and GitHub Actions.

> **Current status:** First executable integration slice. The weekly/manual workflow can launch a read-only Omnara research agent after repository configuration. Defense, authorized red-team, independent evaluation, staging isolation, event collection, and merge enforcement are not yet implemented.

## What is implemented

- Omnara REST launch adapter using the official documented `POST /orgs/{orgID}/projects/{projectID}/agents` contract.
- Research-only agent with web search and web fetch tools; no shell, machine, GitHub write access, scanners, or production access.
- GitHub Actions manual and weekly launch workflow with least-privilege permissions.
- Idempotent launch requests, bounded timeouts, input validation, and unit tests.
- Fail-closed behavior when Omnara configuration is incomplete.

## Configure

Add the Actions secret `OMNARA_API_TOKEN` and repository variables `OMNARA_ORG_ID`, `OMNARA_PROJECT_ID`, `OMNARA_MODEL_PROVIDER_CONFIG`, and `OMNARA_MODEL_NAME`. Optionally set `OMNARA_API_URL` for a self-hosted deployment. See [Omnara integration](docs/omnara-integration.md).

## Run tests

```bash
python3 -m unittest discover -v
```

## Safety invariants

- Research agent is read-only and may use only public web research tools.
- No production credentials, customer media, DRM keys, or production database access.
- Red-team tests only on StreamShield-owned, explicitly authorized synthetic staging.
- Screen recording by an authorized viewer and external-camera recording are accepted limitations, not vulnerabilities or release blockers.
- No absolute copy-prevention claims.
- Automatic merge remains disabled until independent evaluation, required checks, branch protection, and rollback are verified.

See [architecture](docs/architecture.md), [security policy](docs/security-policy.md), and [accepted security exceptions](security-evolution/architecture/security-exceptions.md).
