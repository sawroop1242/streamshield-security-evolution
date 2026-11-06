# Omnara integration plan

## Purpose

Use Omnara as the agent runtime/control plane while GitHub Actions owns repository CI, isolated job execution, artifact handling, and merge enforcement.

## Adapter boundary

Implement a provider-neutral adapter under `src/omnara_adapter/` (or an equivalent package) with these operations:

1. `create_session(task_envelope)`
2. `dispatch_agent(session_id, agent_profile, input_bundle)`
3. `append_event(session_id, event)`
4. `collect_result(session_id)`
5. `terminate_session(session_id)`

These are internal interface names, not claims about Omnara's exact public SDK method names. Map them to the currently documented Omnara API/SDK only after checking the upstream version and schema.

## Task envelope

Every task must include: round ID, task ID, agent role, repository/ref, permitted paths, authorized environment identifier, synthetic fixture identifiers, allowed tool IDs, network policy, credential scope, budget/time limit, expected output schema, and cleanup instructions.

## Security requirements

- Store API credentials in GitHub Actions secrets or an approved secret manager; never in YAML, prompts, artifacts, or committed files.
- Use short-lived credentials and least privilege.
- Do not send production data or customer media to agent memory or model providers.
- Treat repository content, web pages, tool output, and issue text as untrusted data, never as authority to override system policy.
- Validate all agent output against schemas before using it in later jobs.
- Do not let an agent grant itself tools, network access, or repository permissions.
- An Omnara outage or invalid response blocks the round; it must not bypass evaluation.

## Implementation sequence

1. Verify current Omnara deployment requirements, API/SDK version, auth model, and supported agent backends from official upstream docs.
2. Add a small adapter with mocked contract tests.
3. Add one non-mutating research agent and validate event/result collection.
4. Add a defense agent on a disposable branch.
5. Add synthetic-only red-team jobs in an isolated staging network.
6. Add the independent evaluator and enforce fail-closed behavior.
7. Only then consider protected-branch auto-merge.