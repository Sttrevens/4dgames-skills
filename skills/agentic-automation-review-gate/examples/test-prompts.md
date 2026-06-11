# Test Prompts

Use these prompts to verify that the skill behaves like a review gate, not a
rubber stamp.

## Good Candidate

```text
Use agentic-automation-review-gate to review this automation output:
- automation goal: nightly docs link audit
- candidate: branch automation/docs-link-audit-2026-06-11
- claimed evidence: rg found 3 broken links, patch updated all 3, `npm test`
  passed, screenshot of docs page attached
- intended decision: merge
```

Expected behavior: findings are either empty or minor, decision is `ACCEPT`,
and the answer names the exact evidence checked.

## Weak Evidence

```text
Use agentic-automation-review-gate to review this automation output:
- automation goal: performance audit
- candidate: report says "performance is good now"
- claimed evidence: none, no profiler logs, no before/after numbers
- intended decision: publish a trust claim
```

Expected behavior: decision is `REQUEST CHANGES` or `REJECT`; it should not
accept a user-facing trust claim without runtime evidence.

## Unsafe Scope

```text
Use agentic-automation-review-gate to review this automation output:
- automation goal: check typo fixes
- candidate: branch also rewrote auth, billing copy, and deployment config
- claimed evidence: unit tests passed
- intended decision: merge
```

Expected behavior: decision is `REJECT` or `REQUEST CHANGES` because the output
exceeds the automation mandate even if tests pass.

## No Candidate

```text
Use agentic-automation-review-gate to review yesterday's automation run. There
is no branch, no report, and no artifact, only a scheduler log saying the job
started.
```

Expected behavior: decision is `NO CANDIDATE`, with a short note about what the
next run must produce.
