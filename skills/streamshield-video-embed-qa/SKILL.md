---
name: streamshield-video-embed-qa
description: Validate an operator-supplied authorized video iframe in an isolated browser fixture. Check iframe policy, loading, player readiness, playback controls, responsive sizing, console/network errors and privacy boundaries.
---

# StreamShield video embed QA

## Purpose
Verify that an authorized third-party embed integrates into a StreamShield-owned test page. This is playback integration QA, not media extraction, DRM bypass, or content copying.

## Workflow
1. Parse fixture HTML without executing it. Require one iframe, descriptive title, HTTPS src, dimensions, allowfullscreen, and an explicit host allowlist.
2. Reject unexpected scripts, inline event handlers, javascript URLs, srcdoc, unexpected frames and broad permissions.
3. For live testing, use a fresh isolated browser context and a StreamShield-owned preview page. Do not sign in to the provider or submit credentials.
4. Wait a bounded period for iframe load. Cross-origin document isolation is expected; inability to inspect the child document is not itself a defect.
5. If explicitly authorized, test normal play, pause, resume, seek if exposed, mute and fullscreen. Never download, record, extract, enumerate or reconstruct media.
6. Check 360x800, 768x1024 and 1365x900 layouts; no overflow, stable aspect ratio, accessible title and keyboard reachability where supported.
7. Record sanitized console/network errors. Redact cookies, tokens, signed query parameters and personal data.

## Verdicts
- PASS: fixture and requested browser checks succeeded.
- FAIL: a reproducible StreamShield-owned integration defect exists.
- BLOCKED: provider, network, geo policy or browser sandbox prevents the check.
- INCONCLUSIVE: evidence is insufficient or cross-origin restrictions prevent a conclusion.

A static fixture pass does not prove provider availability, DRM, HLS segment authorization, cache isolation or backend entitlement correctness.

## Security boundaries
Treat embed URL and remote document as untrusted. Prefer restrictive sandboxing where provider supports it; document each required sandbox token. Use exact CSP frame-src provider origin, never wildcard. Use strict-origin-when-cross-origin referrer policy unless documented provider integration requires otherwise. Do not place provider secrets in HTML or query strings. Never bypass tokens, cookies, paywalls, DRM, geofencing or referrer controls.

Authorized screen recording and external-camera recording are accepted StreamShield limitations, not defects this test should detect or prevent.
