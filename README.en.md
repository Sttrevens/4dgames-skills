# 4D Games Skills

[中文](README.md)

4D Games Skills is a public index of reusable agent skills from 4D Games'
game-development, agent-automation, and personal-systems workflows.

The goal is not to collect prompts. Each skill is a compact operating procedure
for an agent: when to use it, what context to inspect, how to act, and what
verification or handoff should exist before the work is considered useful.

## Install

For now, install a skill by pointing your agent or skills CLI at the relevant
directory under `skills/`.

```bash
# Example path
skills/air-game-dev-pm
```

## Skills

<!-- SKILLS:START -->
| Skill | Category | Description |
|---|---|---|
| [`agentic-automation-review-gate`](skills/agentic-automation-review-gate) | Agent Operations | Review recurring agent automation output before merge, deployment, or user-facing trust claims. |
| [`4d-bot-integration`](skills/4d-bot-integration) | Bot Runtime | Work safely with 4D Games bot runtimes, Feishu/Lark channel workers, tenant boundaries, and Codex worker handoffs. |
| [`steam-launch-forecast`](skills/steam-launch-forecast) | Game Business | Forecast Steam launch performance from wishlists, Steam/community signals, regional demand, and comparable games. |
| [`air-game-dev-pm`](skills/air-game-dev-pm) | Game Production | Plan game development from player experience into mainstays, features, validation levels, tasks, and iteration stones. |
| [`learning-project-planner`](skills/learning-project-planner) | Personal Systems | Turn a study topic into a durable learning project with roadmap, context, dashboard, and first-week lesson. |
| [`personal-health-pulse`](skills/personal-health-pulse) | Personal Systems | Build or operate a local-first personal health tracking and coaching agent across any supported channel. |
<!-- SKILLS:END -->

## Design Principles

- Keep `SKILL.md` concise enough for agent context windows.
- Move long schemas, examples, and implementation details into `references/`.
- Do not publish private paths, user IDs, tenant IDs, chat logs, customer data,
  API tokens, or internal deployment secrets.
- Favor workflows that create evidence: tests, screenshots, reports, branch
  names, acceptance criteria, rollback signals, or next-stone handoffs.
- Treat local-first trust as a product feature, not an afterthought.

## Development

Edit `skills.yaml` and the corresponding `skills/<name>/SKILL.md`. Then run:

```bash
python3 scripts/render_readme.py
python3 scripts/validate_skills.py
```

Both README files are rendered from `skills.yaml`.

