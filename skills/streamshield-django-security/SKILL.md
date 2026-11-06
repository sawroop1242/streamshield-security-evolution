---
name: streamshield-django-security
description: Review StreamShield Django APIs, tenant boundaries, signed playback sessions, provider integrations, webhooks and media authorization.
---

# StreamShield Django security review

## Authority boundaries
The LMS remains authoritative for identity, enrollment and payment. StreamShield validates the configured integration contract; it does not invent a parallel entitlement authority. Persistent centralized video storage remains Telegram-only unless the product owner changes that decision.

## Review order
1. Map changed views, serializers, middleware, models, tasks, migrations and settings.
2. Trace LMS assertion -> playback authorization -> manifest/segment delivery.
3. Identify tenant, user, asset, session and policy binding at every boundary.
4. Inspect cache keys, CDN headers, redirects, signed URLs, expiry and logs.
5. Review tests for unauthorized, expired, replayed, cross-tenant and revoked sessions.
6. Run project checks and targeted tests; report checks that could not execute.

## Required invariants
- Every playback authorization is scoped to tenant, asset, user/session and expiry.
- Enforce authorization for every protected manifest, segment, subtitle, key/license and download endpoint.
- User-supplied asset IDs never replace entitlement checks.
- Signed tokens have explicit issuer, audience, purpose, expiry and rotation policy.
- Replay and concurrency policy is explicit; retries do not broaden access.
- Cache keys and response headers prevent cross-user and cross-tenant protected cache hits.
- Logs/errors never expose bearer tokens, cookies, signing keys, license challenges or private Telegram references.
- Webhooks verify signatures, timestamp/replay windows and event idempotency.
- Provider callbacks and redirects use allowlisted origins; arbitrary user URLs must not trigger server-side fetches.
- Django templates escape untrusted values; iframe URLs are validated against provider/host allowlists.

## Video delivery checks
Distinguish opaque iframe URLs from direct media manifests. Do not infer HLS/DASH from an /embed/ path. Verify protocol only through authorized browser/network diagnostics. Test manifest and segment authorization independently in synthetic staging. Test token expiry during playback, revocation, cache isolation and cross-tenant denial. Do not classify screen recording or external-camera capture as vulnerabilities.

For each finding include severity, confidence, exact source location, preconditions, impact, safe reproduction and remediation. Separate confirmed defects from hypotheses. Critical/high block; medium requires explicit risk acceptance; low is tracked.
