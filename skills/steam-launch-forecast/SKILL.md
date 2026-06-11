---
name: steam-launch-forecast
description: Use when a user needs a Steam game launch forecast, wishlist-to-sales read, comparable-game analysis, regional demand split, or market signal review for first-week or first-month performance.
---

# Steam Launch Forecast

Use this skill to produce a market-research style forecast for Steam launch
performance. It is strongest when the user provides a Steam page, wishlist
count, launch date, price, publisher, social links, trailer data, or a list of
comparable games.

## Workflow

1. Parse the target game or game set.
   - Names, release dates, prices, wishlist counts, publishers, regions, notes.
   - Treat relative dates using the current date and verify fast-moving data
     online.
2. Build a game profile.
   - Genre, tags, production scale, IP status, localization, demo/Next Fest
     history, publisher credibility, and main audience regions.
3. Collect current signals.
   - Steam page, SteamDB followers, wishlist rank when visible, discussions,
     reviews/CCU if released, launch discount, supported languages.
   - YouTube, Bilibili, Reddit, Discord, creator coverage, press, and community
     heat when relevant.
4. Build a dynamic comparable set.
   - Use 3-7 recent comparables, preferably within 6-24 months.
   - Match genre, price, scale, audience region, visibility path, and launch
     condition.
5. Model the funnel.
   - Wishlists are an input, not the answer.
   - Adjust by wishlist freshness, genre conversion, price, review risk,
     Steam visibility, creator coverage, localization, and regional split.
6. Output a forecast.

## Required Output

```text
Game:
Launch status:
Known inputs:
Comparable logic:
Funnel read:
First-week forecast:
Confidence:
Main risks / upside triggers:
```

For multiple games, add a ranking table first.

## Rules

- Prefer ranges over false precision.
- Say what data is missing.
- Separate China-facing and Western/global demand when evidence supports it.
- Do not make investment or publishing claims from wishlist count alone.

## Common Failure Modes

- Converting wishlists to sales with one fixed multiplier.
- Using old comparables when the genre or Steam visibility environment changed.
- Treating Western press silence as global demand weakness for China-facing games.
- Inventing private wishlist rank, revenue, or publisher data.
