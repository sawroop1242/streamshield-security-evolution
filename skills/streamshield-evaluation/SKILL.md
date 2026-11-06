---
name: streamshield-evaluation
description: Independently grade StreamShield security-evolution agent output and pull requests using evidence, deterministic checks and regression evaluations.
---

# StreamShield independent evaluation

The evaluator must not author the candidate or share its mutable workspace. It receives a pinned base SHA, candidate SHA, task contract, test evidence and declared staging scope. It reads and grades; it does not edit or approve itself.

## Sequence
1. Verify repository, base SHA, candidate SHA and changed-file list.
2. Verify authorization. If staging ownership cannot be established, return BLOCKED.
3. Inspect the diff for secrets, scope expansion, workflow permissions, untrusted input handling and policy regressions.
4. Re-run deterministic tests and relevant security checks in a clean job.
5. Map every acceptance criterion to an evidence artifact and exact result.
6. Check regression coverage and whether tests exercise changed behavior.
7. Check that no security invariant or accepted-risk boundary was weakened.
8. Emit an immutable decision artifact tied to candidate SHA.

## Verdicts
PASS: all required checks and evidence pass; no unresolved critical/high finding.
PASS_WITH_ACCEPTED_RISK: named risk has explicit owner approval and bounded mitigation.
FAIL: required check failed or confirmed blocking defect exists.
INCONCLUSIVE: evidence is missing or non-deterministic.
BLOCKED: authorization, isolation or scope is not established.

Only PASS is eligible for a later merge gate. Missing evidence, skipped tests, tool errors and evaluator timeouts never become success.

Track task completion, evidence completeness, defect escape rate, false positives, regressions, evaluator disagreement and cost per accepted change. Do not optimize for raw findings or PR count.

Use synthetic media and identities. Redact tokens, cookies, PII and private asset references. Screen recording and external-camera capture by authorized viewers are accepted limitations, not defects.
