# Test Prompts

Use these prompts to verify that the skill gives ranges, comparables, and
uncertainty instead of a single overconfident number.

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

Expected behavior: separates actual observed performance from pre-launch
signals and updates the funnel assumptions.

## Regional Split

```text
Use steam-launch-forecast for a Chinese-language-heavy detective RPG with
modest Western press but strong Bilibili creator coverage.
```

Expected behavior: separates China-facing and Western/global demand and avoids
using Western press silence as the only demand signal.
