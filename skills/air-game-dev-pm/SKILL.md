---
name: air-game-dev-pm
description: Air's game-development project management method for structuring game ideas, milestones, sprint plans, feature roadmaps, production audits, MVP/prototype scope, and team task breakdowns.
---

# Air Game Development PM

Use this skill to turn a game vision into trackable production work without
losing the player experience. It is especially useful for indie, small-team, or
hybrid AI-assisted game projects where design, code, art, and validation must
stay visible and reversible.

## Principles

1. Start from the farthest foreseeable player experience, not a feature pile.
2. Use the lowest-cost validation that can answer the current risk.
3. Cross the river by feeling the stones: every iteration should create a
   playable or inspectable proof.
4. Keep production continuously trackable with levels, owners, statuses, and
   evidence.

## Workflow

1. Define the Experience.
   - Player view: fantasy, actions, session rhythm, emotional arc.
   - Designer/system view: systems, constraints, novelty, difficulty.
   - User story: one concrete play sequence from start to payoff.
   - Assumptions, validation, and rollback signal.
2. Split the game into Mainstays.
   - Examples: core loop, live/audience loop, level progression, meta
     progression, tech capability.
3. Split Mainstays into Features.
   - `F-*` for player-facing features.
   - `C-*` for capability features such as networking, save, AI, tooling, or
     performance.
4. Assign validation Levels.
   - `L1`: concept case.
   - `L2`: concept prototype / graybox proof.
   - `L3`: stable implementation.
   - `L4`: polish / shippable quality.
5. Break Features into executable Tasks only after the conceptual split is
   clear.
6. Plan Iters so each one produces a playable or inspectable stone.

## Output Shape

```markdown
## Experience
- Farthest foreseeable player experience:
- Player actions:
- Emotional arc:
- Concrete user story:
- Designer/system differences:
- Key assumptions:
- Lowest-cost validation:
- Rollback signal:

## Mainstays
| Mainstay ID | Name | Experience role | Owner |
|---|---|---|---|

## Features
| Feature ID | Name | Mainstay | Type F/C | Depends on | Current L | Target L | Owner | Iter | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|

## Iter N
- Goal:
- Target experience:
- Features raised:
- Output:
- Validation:
- Rollback condition:
```

## Review Checklist

- Does the plan begin with player experience?
- Are assumptions explicit and ordered by risk?
- Is the validation cheaper than full production?
- Are Levels used as validation state, not percent-complete theater?
- Is the plan balanced across Mainstays?
- Does each Iter produce a playable or inspectable stone?
- Is the rollback point clear?

