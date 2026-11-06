# Initial threat model

Scope: StreamShield application and authorized staging environment. This is a starting inventory, not a claim that every control exists.

Threat areas:

1. Unauthorized playback and object-level authorization failures.
2. Cross-tenant data access and shared-cache leakage.
3. Playlist/segment authorization gaps, token replay, range-request abuse, and stale authorization.
4. Session sharing, credential abuse, and enrollment revocation failures.
5. Telegram-origin exposure and metadata-to-asset mapping errors.
6. Untrusted community cache/P2P peers and media integrity failures.
7. Mobile offline-license lifecycle, device binding, expiry, and encrypted storage.
8. Secrets in source, CI logs, artifacts, error responses, and configuration.
9. Abuse of agent tools, prompt injection from untrusted content, and CI credential escalation.

Accepted residual risks: authorized-viewer screen recording and external-camera recording. See `security-evolution/architecture/security-exceptions.md`.

All testing uses synthetic accounts, tenants, and media in explicitly authorized staging. Record controls, evidence, severity, reproducibility, and residual risk for each finding.