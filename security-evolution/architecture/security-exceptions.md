# Accepted security exceptions

## SE-001: Screen recording and external-camera recording

**Status:** Accepted risk / not a release blocker.

An authorized viewer who can legitimately receive and render video may capture it using operating-system or device-level screen recording, or an external camera. StreamShield accepts this limitation.

### Required handling

- Do not classify legitimate screen recording by an authorized viewer as a vulnerability.
- Do not include screen recording as a red-team failure or release-blocking test.
- Do not ask defense agents to defeat OS/device screen-recording capabilities.
- External-camera recording is also an accepted limitation.

### Scope boundary

This exception does not permit or excuse unauthorized API access, unauthorized playlist or segment retrieval, token replay, cache leakage, session sharing, cross-tenant access, unauthorized license use, or reconstruction through unauthorized access to delivered media.

The product must not claim absolute copy prevention. It should protect authorization and delivery paths, detect abuse where practical, and state residual capture risk honestly.