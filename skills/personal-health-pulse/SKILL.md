---
name: personal-health-pulse
description: Build or operate a channel-agnostic personal health tracking and coaching agent for nutrition, training, sleep, recovery, reminders, scoring, and weekly self-review.
---

# Personal Health Pulse

Use this skill to build or operate a local-first personal health pulse system.
The system listens through whatever channel the host agent supports, records
health check-ins into structured local files, and replies with warm, concise
coaching.

## Operating Rules

- Keep records local by default unless the user explicitly chooses a remote
  store.
- Treat advice as coaching and self-review, not medical diagnosis.
- Do not shame the user.
- Avoid hidden state in conversation memory; durable rules and long-term facts
  belong in project docs or structured data.
- Prefer structured records for anything that will be scored or summarized.
- Never publish user IDs, chat IDs, private paths, examples, or personal health
  facts in reusable artifacts.

## Workflow

1. Identify the user's goal, constraints, channel, and preferred data store.
2. Define data files for daily records, workouts, body measurements, food
   references, derived assessments, and weekly reviews.
3. Route each incoming message:
   - simple question: answer from recent context;
   - record update: persist data, then reply;
   - rich review: inspect image/product/restaurant/scoring context;
   - system request: update the project or reminder workflow.
4. Score only when appropriate.
   - Official daily scores wait until the day is closed.
   - Provisional scores must be labeled.
   - Ordinary unrelated questions do not need a score.
5. Plan reminders with intent first, then adapter details.
6. Build failure recovery.
   - Deduplicate messages.
   - Recover stale processing records.
   - Send a short fallback on timeout.
   - Keep audit logs for manual inspection.

## Suggested Files

```text
data/daily.csv
data/workouts.csv
data/body_measurements.csv
data/food_references.jsonl
data/daily_assessments.jsonl
data/pending_messages.jsonl
data/inbox.jsonl
docs/scoring_rubric.md
docs/agent_workflow.md
```

## Reply Style

Warm, grounded, and brief. Reflect the user's situation, record what matters,
then give one or two concrete next actions.

