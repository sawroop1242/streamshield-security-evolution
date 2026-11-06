# Architecture

## Control plane

GitHub Actions is the job scheduler and CI execution layer. Omnara is the agent lifecycle/session layer, subject to a separately implemented and tested adapter. Agents run as isolated jobs or isolated remote workspaces; they do not share mutable credentials or a privileged machine.

```text
GitHub events / schedule
        |
        v
Round orchestrator
        |
        +--> Research and tool discovery
        +--> Defense agents (scoped branches)
        +--> Red-team agents (synthetic staging only)
        |
        v
Evidence store + shared intelligence (versioned files/artifacts)
        |
        v
Independent evaluator
        |
        v
Required CI checks + policy gate
        |
        v
Protected pull request -> conditional merge
```

## Roles

- Five defense agents: architect, Django, streaming/gateway, DRM/playback, reviewer.
- Five red-team agents: browser, HLS, API, session/token, reconstruction/evidence.
- One independent evaluator.
- An orchestrator assigns immutable task IDs, scope, environment, budget, deadline, allowed tools, and expected evidence.

## Execution model

- Use separate GitHub Actions jobs/runners for independent tasks.
- Use Omnara for agent sessions, event history, and supported agent orchestration after its integration is implemented.
- Use GitHub artifacts for temporary test outputs with retention limits; commit sanitized, durable reports to the repository.
- Pin third-party actions to full commit SHAs before production use. The starter workflows are intentionally minimal and must be hardened.
- Do not execute untrusted pull-request code with privileged secrets or write tokens.

## Merge policy

Only an independent evaluator result of `PASS` is eligible for automatic merge. `PASS_WITH_ACCEPTED_RISK` requires a separately documented policy decision and cannot contain unresolved critical/high findings. `FAIL`, `INCONCLUSIVE`, `BLOCKED`, missing evidence, missing evaluator, or failed CI blocks merge.

## Product architecture constraints

- Django reusable package/API; existing LMS owns identity, enrollment, and payment authority.
- Player-first hybrid delivery; preserve playback continuity and authorized seeking.
- Telegram is the only approved persistent centralized video storage in the current product decisions.
- Any community cache or P2P path must be opt-in, integrity-checked, and independently authorized.
- Do not store customer video or production secrets in Omnara memory, model prompts, logs, or artifacts.