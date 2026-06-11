# 4D Bot Integration Skill

Work on bot runtimes without collapsing personal agents, internal project bots,
and customer-facing channels into the same unsafe message path.

## 10-Second Proof

The skill produces a runtime read like this before recommending changes:

```text
Entry:
Worker:
Send/callback:
Tenant boundary:
Tool boundary:
Risk:
Verification:
Rollback:
```

That map is the visible artifact: it shows where a message enters, which worker
handles it, what identity and tenant it carries, and what can safely send back.

## Why Install It

Bot integration work is deceptively easy to demo and easy to break in
production. This skill keeps tenant isolation, sender identity, callback scope,
tool permissions, and Codex/Claude worker handoffs explicit before code changes.

## Use When

- Understanding or modifying bot runtime architecture.
- Routing messages between Feishu/Lark channels and agent workers.
- Checking tenant, sender, callback, quota, and tool bridge boundaries.
- Comparing a lightweight personal agent inbox with a production bot runtime.

## Minimum Run

```text
Use 4d-bot-integration to review this bot architecture/change:
- repo/path:
- channel: Feishu/Lark / WeCom / personal inbox / other
- worker runtime: Gemini / Codex / Claude / local command
- intended change:
- production risk:
```

## Safety Boundary

The skill must not expose tenant config, customer chat content, webhook secrets,
API tokens, or deployment credentials. It should prefer dry runs and contract
tests over real sends unless the user explicitly authorizes a production action.

## Verification Assets

- [`examples/test-prompts.md`](examples/test-prompts.md) covers architecture
  read, Codex worker handoff, tenant-boundary review, and unsafe-send cases.

## Install

Point your agent or skills CLI at this repository. The skill entrypoint is:

```text
SKILL.md
```

Part of the [4D Games Skills](https://github.com/Sttrevens/4dgames-skills)
index.
