# Test Prompts

Use these prompts to verify that the skill gives ranges, comparables, an
explicit knowledge boundary, and uncertainty instead of a single overconfident
number.

## Known Wishlist Count

```text
Use steam-launch-forecast for a $14.99 co-op horror game launching in two
months. Known inputs: 80,000 wishlists, English + Simplified Chinese support,
Next Fest demo, 20k Discord members, no publisher.
```

Expected behavior: forecast is a range; explains wishlist freshness, genre
conversion, demo quality risk, and China/global split.

## Missing Wishlist Count

```text
Use steam-launch-forecast for this Steam page: [url]. We do not know wishlists.
Estimate launch potential from public signals only.
```

Expected behavior: does not invent wishlists; uses SteamDB/community/social
signals and marks confidence lower.

## Released Game Readback

```text
Use steam-launch-forecast to analyze a game that launched last week. Compare the
forecast logic against actual reviews, CCU, and community reaction.
```

Expected behavior: labels this `post_launch_nowcast` or
`retrospective_backcast`; separates actual observed performance from pre-launch
signals; and does not call the result an unbiased blind forecast.

## Same Day Snapshot Leakage Check

```text
Use steam-launch-forecast for a game releasing today. The only wishlist count is
a public source marked with today's date, but it gives no capture time or time
zone. Treat this as a blind pre-launch forecast and calculate conversion after
the first week.
```

Expected behavior: does not call the result blind-prelaunch without proving the
snapshot preceded release in an explicit IANA time zone. It should mark the
evidence provisional or switch to a backcast/nowcast, and call
`first-week units / prelaunch wishlist snapshot` a snapshot-normalized sales
ratio rather than cohort conversion.

## Released Game Forecast Boundary

```text
This game launched last week. Use its current review count and concurrent-player
peak to produce an unbiased forecast as if we were deciding before launch.
```

Expected behavior: refuses the blind-forecast label because the requested
signals are post-launch. It may provide a post-launch nowcast or a clearly
labeled retrospective backcast with a stated knowledge cutoff.

## Regional Split

```text
Use steam-launch-forecast for a Chinese-language-heavy detective RPG with
modest Western press but strong Bilibili creator coverage.
```

Expected behavior: separates China-facing and Western/global demand and avoids
using Western press silence as the only demand signal.
