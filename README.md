# StreamShield Security Evolution

An open-source control plane for autonomous, evidence-driven security improvement of StreamShield, using Omnara-managed agents and GitHub Actions.

> Current status: The Omnara research-agent adapter and initial ECC-inspired StreamShield skills are implemented on the feature branch. The research workflow requires Omnara configuration. Defense, authorized red-team, independent evaluator execution, isolated staging, event collection and merge enforcement are not yet operational.

## Implemented
- Documented Omnara REST launch adapter for a read-only research agent.
- Weekly/manual GitHub Actions workflow with least-privilege permissions.
- Unit tests for Omnara request construction and fail-closed behavior.
- StreamShield-specific skills for Django security, video iframe QA and independent evaluation.
- Specialized Django security-reviewer and video-embed-QA agent prompts.
- Static fixture for the owner-supplied video embed and HTML validation tests.
- ECC adoption notes describing the patterns adapted.

## Configure Omnara
Add Actions secret OMNARA_API_TOKEN and repository variables OMNARA_ORG_ID, OMNARA_PROJECT_ID, OMNARA_MODEL_PROVIDER_CONFIG and OMNARA_MODEL_NAME. See docs/omnara-integration.md.

## Run tests
python3 -m unittest discover -v

## Safety invariants
- Research agent is read-only and may use only public web research tools.
- No production credentials, customer media, DRM keys or production database access.
- Red-team tests only on StreamShield-owned, explicitly authorized synthetic staging.
- Screen recording by an authorized viewer and external-camera recording are accepted limitations, not vulnerabilities or release blockers.
- No absolute copy-prevention claims.
- Automatic merge remains disabled until independent evaluation, required checks, branch protection and rollback are verified.

See docs/ecc-adoption.md, docs/architecture.md, docs/security-policy.md and security-evolution/architecture/security-exceptions.md.
