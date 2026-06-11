---
name: "4d-bot-integration"
description: Use when working with 4D Games bot runtimes, Feishu/Lark bot channels, Codex worker handoffs, tenant isolation, message routing, and production bot safety boundaries.
---

# 4D Bot Integration

Use this skill when working with 4D Games bot runtimes or related Feishu/Lark
channel workers. The skill is intentionally conservative: production bot
systems carry tenant, customer, permission, and message-delivery risk.

## Scope

Use for:

- understanding bot runtime architecture;
- routing messages between Feishu/Lark channels and agent workers;
- integrating Codex/AI workers behind a bot gateway;
- evaluating tenant isolation, sender identity, callback, quota, and tool
  bridge boundaries;
- comparing a lightweight personal agent inbox with a production bot runtime.

Do not use this skill to expose private tenant config, customer chat content,
API tokens, webhook secrets, or internal deployment credentials.

## Workflow

1. Orient in the target repo.
   - Read `README.md`, `AGENTS.md`, `CLAUDE.md`, and any bot prompt/runtime
     docs the repo provides.
   - Identify whether the project is a production bot, a local worker, a
     sidecar, or a personal automation.
2. Map the message path.
   - inbound channel;
   - normalized message envelope;
   - tenant/user identity;
   - agent worker call;
   - callback/send path;
   - logging and failure recovery.
3. Check boundaries.
   - Does the worker know which tenant/chat/user it serves?
   - Are tools scoped by tenant and permission?
   - Are customer messages separated from local/personal experiments?
   - Is there a kill switch or fallback behavior?
4. Make changes only when the requested scope is explicit.
   - Prefer small adapters and contracts over broad runtime rewrites.
   - Do not mix personal health/project automations into customer bot runtime
     paths unless the user has explicitly approved that architecture.
5. Verify with safe tests or dry runs.
   - Unit tests for routing and permission rules;
   - dry-run sends where possible;
   - log inspection without dumping private message bodies;
   - explicit residual risk.

## Output Shape

```markdown
## Runtime Read
- Entry:
- Worker:
- Send/callback:
- Tenant boundary:
- Tool boundary:

## Change Or Recommendation
- Scope:
- Files likely involved:
- Risk:
- Verification:
- Rollback:
```

## Design Bias

Keep personal agents, customer bots, and internal project bots separate unless a
clear product decision says otherwise. Shared libraries are fine; shared
production message paths are not the default.

## Common Failure Modes

- Adding a worker before mapping send/callback identity.
- Mixing tenant memory, tools, or logs for convenience.
- Testing by sending into a real group before dry-run verification.
- Copying personal-agent behavior into a customer bot runtime without explicit
  product approval.
