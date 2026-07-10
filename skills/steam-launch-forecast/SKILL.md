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
2. Set the forecast boundary before interpreting signals.
   - Declare `Forecast mode`: `blind_prelaunch`, `retrospective_backcast`, or
     `post_launch_nowcast`.
   - Record a `Knowledge cutoff`: the latest instant at which a permitted input
     was public or available. Only `blind_prelaunch` is eligible to be described
     or scored as a blind forecast.
   - A date-only source captured on release day is not blind-prelaunch evidence
     unless its order relative to the release is demonstrated with a timestamp
     and IANA time zone.
3. Build a game profile.
   - Genre, tags, production scale, IP status, localization, demo/Next Fest
     history, publisher credibility, and main audience regions.
4. Collect permitted signals.
   - Steam page, SteamDB followers, wishlist rank when visible, discussions,
     reviews/CCU if released, launch discount, supported languages.
   - YouTube, Bilibili, Reddit, Discord, creator coverage, press, and community
     heat when relevant.
   - Mark each material input as verified, provisional, unverified, or disputed;
     exclude disputed inputs from the estimate.
   - In `blind_prelaunch` mode, do not use post-launch reviews, CCU, sales, or
     any signal published after the knowledge cutoff.
5. Build a dynamic comparable set.
   - Use 3-7 recent comparables, preferably within 6-24 months.
   - Match genre, price, scale, audience region, visibility path, and launch
     condition.
6. Model the funnel.
   - Wishlists are an input, not the answer.
   - Adjust by wishlist freshness, genre conversion, price, review risk,
     Steam visibility, creator coverage, localization, and regional split.
   - If calculating `first-week units / prelaunch wishlist snapshot`, call it a
     snapshot-normalized sales ratio, not cohort conversion.
7. Output a forecast.

## Required Output

```text
Game:
Launch status:
Forecast mode:
Knowledge cutoff:
Evidence tier:
Calibration eligibility:
Known inputs:
Comparable logic:
Funnel read:
First-week forecast:
Confidence:
Main risks / upside triggers:
```

For multiple games, add a ranking table first.

Use [the calibration contract](references/calibration-contract.md) when the
request compares forecasts with outcomes, audits a prior call, or adds a result
to a calibration dataset.

## Rules

- Prefer ranges over false precision.
- Say what data is missing.
- Separate China-facing and Western/global demand when evidence supports it.
- Do not make investment or publishing claims from wishlist count alone.
- Keep the forecast issue time separate from the knowledge cutoff and cite the
  source and capture time for material inputs.
- Call a released-game analysis `post_launch_nowcast` or
  `retrospective_backcast`; never present it as a blind forecast.
- Do not call an estimate unbiased without a stated benchmark and error method;
  a post-launch nowcast is never an unbiased blind forecast.
- Label calibration provisional when actuals are not verified or the sample is
  too small to generalize.

## Common Failure Modes

- Converting wishlists to sales with one fixed multiplier.
- Using old comparables when the genre or Steam visibility environment changed.
- Treating Western press silence as global demand weakness for China-facing games.
- Inventing private wishlist rank, revenue, or publisher data.
- Calling a same-day, date-only snapshot pre-launch without proving the time
  order.
- Letting post-launch reviews or CCU leak into a claimed blind forecast.
- Calling a snapshot-normalized sales ratio a conversion rate for a defined
  wishlist cohort.
