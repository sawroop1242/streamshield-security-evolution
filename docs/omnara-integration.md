# Omnara integration

## Verified integration surface

The adapter uses Omnara's documented JSON REST API, not guessed SDK method names.

- Hosted API base: `https://api.omnara.com/v1`
- Self-hosted API base: the deployment origin plus `/api/v1`
- Authentication: `Authorization: Bearer $OMNARA_API_TOKEN`
- Launch: `POST /orgs/{orgID}/projects/{projectID}/agents`
- Agent launch body supports `config_source: { source, source_format }`, `name`, and `message`.
- The launch endpoint accepts an `Idempotency-Key` header.

Contracts were checked against the official Omnara repository:
- [API overview](https://github.com/omnara-ai/omnara/blob/main/docs/api/overview.mdx)
- [Quickstart launch example](https://github.com/omnara-ai/omnara/blob/main/docs/snippets/quickstart-launch.mdx)
- [Published OpenAPI specification](https://github.com/omnara-ai/omnara/blob/main/docs/api-reference/openapi.yaml)

## First implemented agent: research-only

`scripts/launch_omnara_research.py` creates a research agent with only Omnara's documented `web_search` and `web_fetch` built-in tools. It does not attach a machine, GitHub write integration, shell, browser automation, repository credentials, or production access.

The agent's instruction is deliberately limited to public research and evidence synthesis. It cannot create branches, change files, run security probes, or merge code. The supplied workflow scope is treated as untrusted context and cannot override the fixed safety policy.

## GitHub Actions configuration

Set these repository **Actions secrets/variables**:

| Name | Type | Purpose |
| --- | --- | --- |
| `OMNARA_API_TOKEN` | Secret | Omnara personal or appropriately scoped org API key |
| `OMNARA_ORG_ID` | Variable | Omnara organization ID (`org_...`) |
| `OMNARA_PROJECT_ID` | Variable | Omnara project ID (`proj_...`) |
| `OMNARA_MODEL_PROVIDER_CONFIG` | Variable | Existing configured model-provider name in that Omnara project |
| `OMNARA_MODEL_NAME` | Variable | Existing configured model name in that provider |
| `OMNARA_API_URL` | Optional variable | Defaults to hosted API; for self-hosting use the deployment origin plus `/api/v1` |

Never put tokens in repository variables, workflow YAML, agent prompts, or committed files. Use a dedicated least-privilege Omnara API key. The workflow has `contents: read`, disables persisted checkout credentials, and launches only from trusted workflow code on manual dispatch or the weekly schedule.

Run locally:

```bash
python3 -m unittest discover -v
python3 scripts/launch_omnara_research.py
```

The launch script validates public ID formats, requires HTTPS except loopback self-hosting, applies a per-workflow idempotency key, uses a bounded HTTP timeout, and avoids printing bearer credentials.

## Current boundary / not yet enabled

This is the first working integration slice, not the complete autonomous evolution system. The workflow only launches a research agent. It does not yet collect agent events/artifacts, create defense or red-team subagents, provision isolated staging, evaluate pull requests, or merge changes. Those remain separate implementation stages.

Automatic merge remains disabled until independent evaluation, reproducible evidence, required CI, protected-branch rules, and rollback are implemented and tested. Red-team work remains restricted to StreamShield-owned, explicitly authorized synthetic staging. Screen recording and external-camera recording by an authorized viewer remain accepted limitations, not findings or release blockers.
