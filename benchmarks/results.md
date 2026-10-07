# Benchmark results (auto-generated, do not hand-edit)

## EXP01-license-floor — REFUTED-AS-STATED-2026

- interpretation: AED 2,000 < AED 5,750 RAKEZ floor and < AED 11,900 IFZA floor. Only eTrader (1,070, nationals/services) or unlicensed marketplace-testing fits 2,000 in 2026. 2017 regime was looser; survivorship + regime-shift explains gap.

  - claim_AED: 2000

  - legal_min_expat_product_AED: 5750

  - etader_AED: 1070

  - gap_AED: 3750

  - ratio_claim_to_min: 0.348

## EXP02-growth-math — EXTRAORDINARY-OUTLIER

- interpretation: 232.7% CAGR needed to 30M (306.8% to 150M) vs ~19% market (12.25x). At market rate, 2k->30M takes ~55.3 years. Hence claim requires low-base + COVID demand shock + offline leverage + brand intangible (77-80%). Replicable system? No, without same shocks. Repeatable process? Partially (sourcing/support/playbooks).

  - required_cagr_to_30M_pct: 232.67

  - required_cagr_to_150M_pct: 306.8

  - market_cagr_2020_2025_pct: 19.0

  - market_cagr_2026_2031_pct: 11.29

  - multiple_of_market: 12.25

  - years_at_market_rate_to_30M: 55.3

  - intangible_share_30M: 0.8

  - intangible_share_35M: 0.767

## EXP03-4x-resign-rule — SUPPORTED-WITH-STABILITY-CONDITION

- interpretation: 4x = 25% draw + 25% growth + 25% ops + 25% buffer. Sound lean-finance heuristic; matches 12-month stability test in transcript. Fails if profits volatile (must use min-trailing-12mo, not peak month).

  - example_salary: 20000

  - example_net: 80000

  - allocation: {'salary': 20000.0, 'develop': 20000.0, 'ops_reinvest': 20000.0, 'buffer': 20000.0}

  - owner_draw_pct_of_net: 25.0

## EXP04-7day-profit — CLAIMANT-CORRECT-TO-REJECT-7DAY

- interpretation: Shopify 18-24mo runway + 80-90% y1 fail rate corroborate rejecting 7-day profit plans. Correct sequence: cover costs -> break-even -> profit. 40-50k/mo anecdote (2023/24, 2k+2k in) is revenue, not net, and n=1.

  - seven_day_profit_expectation: False

  - benchmark_runway_months: [18, 24]

  - base_fail_rate_pct: [80, 90]

## EXP05-category-80pct — SELLER-SPECIFIC-NOT-MARKET-GENERAL

- interpretation: Home/robot/camera strength is consistent with time-saving + busy-household thesis, but market-wide fastest growth is food (13.16%) and largest share fashion (21.59%). 80% unconditional success prob is uncalibrated; conditional on (right price+demo-video+support+warranty) it becomes plausible niche edge.

  - podcast_pick: ['home products', 'robots', 'cameras']

  - market_largest_share: {'fashion_pct': 21.59}

  - market_fastest_cagr: {'food_pct': 13.16}

  - claimed_prob_pct: 80

## EXP06-channel — SUPPORTED

- interpretation: IG-fast-checkout vs TikTok-viral-no-return matches 78.67% smartphone + 5G/AR shopping; KSA Snapchat lead matches Salla/Zid localization (mada/ApplePay/Tabby). Test: run identical SKU x creative on IG vs TikTok vs Snapchat, compare CTR->CVR, not views.

  - uae: ['Instagram', 'TikTok']

  - ksa: ['Snapchat']

  - smartphone_share_pct: 78.67

## EXP07-unit-economics — 2000-BUYS-22-UNITS-BUT-NOT-LICENSE

- interpretation: AED 2,000 buys ~22 units at 89 landed, needing ~96 sales at 60 margin just to cover cheapest licence. Hence 2,000 = inventory-only test budget, not legal launch budget in 2026.

  - assumptions: {'license_fixed': 5750, 'price': 149, 'landed_unit': 89}

  - break_even_units_to_cover_license: 95.8

  - max_units_on_2000: 22
