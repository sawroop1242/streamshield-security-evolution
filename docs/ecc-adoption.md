# ECC-inspired agent and skill design for StreamShield

## Source review
Reviewed the public affaan-m/ECC repository tree on 2026-11-06. Its README describes a multi-harness agent system with 71 agents, 314 skills, hooks, rules, memory and AgentShield. The repository is MIT-licensed. We reviewed selected agent and skill files rather than importing the entire framework.

Useful patterns:
- Specialized agents with explicit activation criteria, tools, scope and structured output.
- Prompt-injection defense for retrieved files, web pages and other untrusted inputs.
- Framework-specific Django review rather than generic security checklists.
- Test analysis mapping changed behavior to meaningful assertions and error-path coverage.
- Eval-driven development: define acceptance criteria before implementation and use deterministic graders.
- Browser QA that is read-only by default, uses test accounts, tests responsive breakpoints and reports inconclusive results when baselines are absent.
- Skills organized around activation, workflow, safety boundaries and report format.

Reviewed upstream files:
- agents/security-reviewer.md
- agents/django-reviewer.md
- agents/pr-test-analyzer.md
- skills/django-security/SKILL.md
- skills/browser-qa/SKILL.md
- skills/security-review/SKILL.md
- skills/eval-harness/SKILL.md
- skills/remotion-video-creation/SKILL.md
- skills/video-editing/SKILL.md
- skills/agent-security-hardening/SKILL.md

## Adoption decision
Adopt the design patterns, not a wholesale copy of ECC. The new StreamShield skills are original project-specific material. ECC is MIT-licensed; this repository does not vendor its source files or claim ECC authorship.

New additions:
- skills/streamshield-video-embed-qa/SKILL.md
- skills/streamshield-django-security/SKILL.md
- skills/streamshield-evaluation/SKILL.md
- agents/video-embed-qa.md
- agents/django-security-reviewer.md

## User-supplied embed fixture
tests/fixtures/video-embed.html contains the exact embed URL supplied by the project owner:
https://study-space.fembed.co/embed/PMmy_HJkq-N4n

Static unit tests validate HTML structure only. They do not fetch or play the remote embed. Live browser playback is a separate opt-in test against a StreamShield-owned preview page. The current web inspection environment could not fetch the provider URL, so availability and actual playback remain unverified.

## Routing
- Django backend or playback authorization diff: Django Security Reviewer + StreamShield Django Security.
- Iframe/player integration diff: Video Embed QA Agent + Video Embed QA.
- Any agent-generated PR: independent evaluator + StreamShield Evaluation.
- UI preview: browser QA principles adapted to authorized staging.
- Video rendering/Remotion: use a separate media creation workflow.

Do not install every ECC agent. Load only skills relevant to each task to reduce context and avoid excess permissions.
