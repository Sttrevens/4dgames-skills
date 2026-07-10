# Public Calibration Contract

Use this reference when recording, evaluating, or publishing a Steam launch
forecast. It makes forecast timing and evidence quality inspectable without
shipping private game data.

## 1. Declare the forecast mode

| Mode | Meaning | Blind-forecast eligible? |
| --- | --- | --- |
| `blind_prelaunch` | The forecast uses only inputs available before launch. | Yes, if the time boundary is evidenced. |
| `retrospective_backcast` | The forecast recreates a historical decision point. | No; it is a reconstruction. |
| `post_launch_nowcast` | The estimate uses post-launch observations. | No; it describes the current state. |

Record both timestamps:

- `issued_at`: when the forecast was written.
- `knowledge_cutoff_at`: the latest instant at which a permitted input was
  available to the forecaster.

Use an exact timestamp with an IANA time zone where possible (for example,
`2026-07-10T09:00:00+08:00` and `Asia/Shanghai`). Do not use an ambiguous
abbreviation such as `CST`. A date-only source is insufficient to establish
pre-launch ordering on the same day as release unless its capture time and
release order are demonstrated.

## 2. Keep evidence quality separate from the estimate

Assign each material signal and outcome one truth tier:

| Tier | Meaning | Forecast treatment |
| --- | --- | --- |
| `verified` | Source and capture time are attributable and internally consistent. | May support an estimate or scored calibration. |
| `provisional` | Plausible, but timing, scope, or source coverage remains incomplete. | May inform a sensitivity range; state the caveat. |
| `unverified` | Cannot be attributed or checked. | Do not use as a scoring anchor. |
| `disputed` | Conflicts with another credible source or has unresolved definition mismatch. | Exclude until resolved. |

For each material input, preserve a source URL or citation, capture time,
definition, and any transformation. Do not average conflicting sources into a
false certainty.

## 3. Use precise metric names

`first-week units / prelaunch wishlist snapshot` is a
**snapshot-normalized sales ratio**. It is not cohort conversion: the wishlist
snapshot is not a deduplicated, fixed cohort and may differ in timestamp,
coverage, cancellations, and post-launch additions. Name the denominator and
time boundary in every table or chart.

## 4. Score only eligible records

For a comparable set with verified actuals and a fixed definition, record:

- signed error: `forecast midpoint - actual`
- absolute error: `abs(forecast midpoint - actual)`
- APE: `abs(forecast midpoint - actual) / actual` (only when actual is nonzero)
- WAPE: `sum(abs error) / sum(actual)`
- interval hit: whether the actual falls inside the forecast range

If an actual is not verified, retain the forecast record but mark it ineligible
for scored calibration. If the eligible sample is small, state that results are
**provisional and not generalizable**; do not claim a durable model improvement.

## 5. Minimal portable record

```text
forecast_id:
game_identifier:
forecast_mode: blind_prelaunch | retrospective_backcast | post_launch_nowcast
issued_at:
knowledge_cutoff_at:
forecast_range_units:
signal_name:
signal_value:
signal_source:
signal_captured_at:
signal_truth_tier: verified | provisional | unverified | disputed
actual_units:
actual_source:
actual_truth_tier:
model_version:
calibration_eligibility:
notes:
```

## 6. Public/private boundary

Publish the method, definitions, generic templates, and reproducible checks.
Do not publish local filesystem paths, screenshots, private actuals, user or
session identifiers, confidential publisher data, or game-specific calibration
records unless their owners have explicitly approved release.
