# Security and execution policy

## Authorization boundary

Testing is permitted only against StreamShield-owned repositories and explicitly designated staging systems for which the project owner has authorization. No scanning, exploitation, credential testing, or load testing of third-party systems or public targets.

## Data boundary

- Synthetic media, synthetic accounts, and fabricated tenant data only.
- No production database, customer data, DRM keys, session cookies, or production credentials.
- No secrets in logs, reports, commits, prompts, or artifacts.
- Sanitize evidence and apply short artifact retention.

## Tool discovery

Discovered tools start in `UNTRUSTED` state. Before execution, record source, license, version, checksum or immutable release reference, permissions, network needs, data access, expected outputs, and risk classification. Require review before adding tools to the approved registry. Installation is confined to ephemeral sandboxes.

## Network policy

Default deny. Allow only required package registries, official documentation/research sources, GitHub, Omnara endpoints, and the isolated staging target. Red-team network access must not permit arbitrary internet target scanning or pivoting.

## Severity gates

- Critical: stop the round and block merge.
- High: block merge.
- Medium: block by default; only a documented, explicitly approved risk exception may proceed.
- Low: document, assign, and track.

No aggregate score can override a critical/high failure.

## Required merge gates

- Authorized environment and synthetic data verified.
- No exposed secrets or sensitive artifacts.
- No unresolved critical/high finding.
- Tenant isolation and authorization regression tests pass.
- Independent evaluator reproduces the fix and returns `PASS`.
- Required CI checks pass; change is traceable to a task and evidence bundle.
- Rollback path exists.

If any gate cannot be evaluated, fail closed.