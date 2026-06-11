---
name: agentic-automation-review-gate
description: Use when recurring Codex/AI automations produce code, reports, QA evidence, or next-step recommendations that need a human-quality review gate before merge, deployment, publication, or trust claims.
---

# Agentic Automation Review Gate

Use this skill to review output from recurring agent automations. The goal is to
decide whether the automation produced reliable, scoped, and useful work, not
to rubber-stamp it because it ran.

## When To Use

- A background agent opened a branch, commit, PR, report, QA artifact, or
  next-stone recommendation.
- A recurring automation claims a check passed or a product state is ready.
- A bot/agent proposes merge, deployment, publication, outreach, or user-facing
  trust claims.
- The user asks whether an automation is "working", "safe to merge", or "going
  in the right direction".

## Review Stance

Findings first. Prefer concrete bugs, missing evidence, unsafe scope, stale
baseline, undocumented behavior, failed gates, or claims that exceed proof.

Do not merge, deploy, send, publish, or mark a goal complete unless the evidence
supports that exact action.

## Workflow

1. Read the automation prompt/config and its latest memory or handoff.
2. Identify the candidate output.
   - branch/commit/report/artifact/date;
   - workspace and baseline;
   - claimed goal;
   - files or systems touched.
3. Check scope.
   - Is the output inside the automation's mandate?
   - Did it avoid unrelated user work?
   - Did it avoid secrets, private data, broad rewrites, or unapproved external
     actions?
4. Check evidence.
   - Commands/tests run;
   - screenshots or runtime proof when product-facing;
   - docs updated when durable truth changed;
   - residual risk stated honestly.
5. Decide.
   - `ACCEPT`: safe to merge/use/report.
   - `REQUEST CHANGES`: useful direction but blocked by fixable gaps.
   - `REJECT`: wrong scope, unsafe, stale, or not evidenced.
   - `NO CANDIDATE`: nothing new to review.
6. If blocked, write feedback that the next automation run can act on.

## Output Shape

```markdown
## Findings
- [P1/P2/P3] Finding with file, command, artifact, or exact evidence.

## Decision
ACCEPT / REQUEST CHANGES / REJECT / NO CANDIDATE

## Gates Checked
- Scope:
- Baseline:
- Tests/evidence:
- Docs:
- Safety:

## Feedback For Next Run
- Candidate:
- Blocked gate:
- Required change:
- Whether to amend, replace, or abandon:
```

## Hard Rules

- "95% automated" still needs review if the remaining 5% can lose trust.
- Do not infer external events such as payments, sends, customer replies, or
  successful runtime QA without evidence.
- For code branches, stage and merge only explicit intended files.
- For game projects, product-facing claims require playable, runtime, visual, or
  carefully scoped static evidence.

## Common Failure Modes

- Accepting an automation because the scheduler ran, even though there is no
  candidate artifact.
- Treating green tests as enough when the automation changed unrelated scope.
- Letting a report make user-facing trust claims without runtime proof.
- Giving vague feedback that the next automation run cannot execute.
