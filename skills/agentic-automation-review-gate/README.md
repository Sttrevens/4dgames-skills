# Agentic Automation Review Gate Skill

A review gate for recurring AI automations: make the last 5% of trust visible
before code, reports, QA claims, or bot recommendations reach users.

## 10-Second Proof

Give the skill an automation branch, report, or handoff. It returns a
findings-first review with one of four decisions:

```text
ACCEPT / REQUEST CHANGES / REJECT / NO CANDIDATE
```

The output is not a generic summary. It checks scope, baseline, evidence,
documentation, safety, and writes feedback the next automation run can act on.

## Why Install It

Recurring agents are cheap enough to run forever, but cheap work still needs a
trust boundary. This skill gives teams a reusable review ritual for background
agents that touch code, QA, documentation, product claims, or automation memory.

## Use When

- A background agent created a branch, commit, PR, report, or QA artifact.
- An automation claims a system is ready or safe.
- You need a merge/deploy/publish gate for recurring agent work.
- You want feedback that the next automation run can act on.

## Minimum Run

```text
Use agentic-automation-review-gate to review this automation output:
- automation goal: [goal]
- candidate branch/report/artifact: [link or path]
- claimed evidence: [tests, screenshots, logs]
- intended decision: [merge/deploy/publish/report]
```

## Safety Boundary

The skill reviews and recommends. It must not merge, deploy, publish, send
messages, or mark a recurring automation as trusted unless the user explicitly
asks for that follow-up and the evidence supports it.

## Verification Assets

- [`examples/test-prompts.md`](examples/test-prompts.md) contains prompts for a
  good candidate, weak evidence, unsafe scope, and no-candidate review.

## Install

Point your agent or skills CLI at this repository. The skill entrypoint is:

```text
SKILL.md
```

Part of the [4D Games Skills](https://github.com/Sttrevens/4dgames-skills)
index.
