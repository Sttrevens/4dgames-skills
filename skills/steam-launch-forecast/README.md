# Steam Launch Forecast Skill

Forecast Steam launch performance with ranges, comparable games, regional demand
splits, and explicit uncertainty instead of turning wishlists into fake
precision.

## 10-Second Proof

The skill returns a forecast packet:

```text
Game:
Known inputs:
Comparable logic:
Funnel read:
First-week forecast:
First-month forecast:
China / global split:
Confidence:
Main risks / upside triggers:
```

It should explain why the comparable set fits, what signal is missing, and which
assumption would move the forecast most.

## Why Install It

Steam launch calls are easy to overfit. This skill forces the agent to separate
wishlists, SteamDB/community heat, creator coverage, localization, genre
conversion, and recent comparable launches before making a range.

## Use When

- Estimating first-week or first-month Steam launch units.
- Reading wishlist/follower/social signals for a game.
- Comparing a Steam game against recent comparable launches.
- Separating China-facing demand from Western/global demand.

## Minimum Run

```text
Use steam-launch-forecast for this game:
- Steam page: [url]
- wishlist count or rank if known: [number]
- launch date / price / demo history: [details]
- target regions: [China / global / both]
```

## Safety Boundary

The skill can support market research and publishing discussion. It should not
present a forecast as investment advice, guarantee revenue, or infer private
wishlist data that the user did not provide.

## Verification Assets

- [`examples/test-prompts.md`](examples/test-prompts.md) includes forecast
  prompts for known wishlists, missing wishlists, released games, and regional
  split reads.

## Install

Point your agent or skills CLI at this repository. The skill entrypoint is:

```text
SKILL.md
```

Part of the [4D Games Skills](https://github.com/Sttrevens/4dgames-skills)
index.
