# Skill Release Gate

Use this gate before publishing or announcing a 4D Games skill. The goal is to
turn a private workflow that works once into a public artifact that strangers
can understand, install, verify, and reuse.

## Eight Questions

1. **User:** who will actually use this skill?
2. **Install reason:** why should they install it instead of asking an agent ad hoc?
3. **One-line hook:** can the value be explained in one sentence?
4. **Visible artifact:** what can someone see in 10 seconds: screenshot, HTML,
   report, diff, dashboard, replay, or forecast?
5. **Minimum run:** what is the shortest prompt or command that closes one loop?
6. **Failure modes:** where does this skill commonly overreach, hallucinate, or
   produce unsafe work?
7. **Safety boundary:** what data, credentials, sends, deploys, or production
   actions are explicitly out of scope without user approval?
8. **Verification:** what test prompt, sample input, expected output, or runtime
   proof shows that the skill works?

## README Baseline

Every public skill repository should make these visible near the top:

- one sentence that names the real user problem;
- a "10-second proof" section with concrete output;
- install path and minimum prompt;
- files or artifacts created by the skill;
- safety boundary;
- examples or test prompts.

## SKILL.md Baseline

- Frontmatter `description` starts with `Use when...` and describes triggering
  situations, not the whole workflow.
- Body stays compact enough for an agent context window.
- Failure modes and verification are explicit.
- Scripts are used for deterministic artifacts instead of hand-written repeated
  HTML, reports, or calculations.

## Release Decision

- **Publish:** all eight questions have concrete answers and the minimum run was
  checked.
- **Soft publish:** value is clear but showcase or validation is thin; label the
  repo as early and add a next-demo task.
- **Hold:** no clear install reason, no visible artifact, or unsafe boundaries.
