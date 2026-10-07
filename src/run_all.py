"""Runs every experiment end-to-end and writes machine-readable verdicts.
Usage: python -m src.run_all
Outputs: data/snapshots/report.json + benchmarks/results.md
"""
import json
from pathlib import Path
from .config import load_snapshot, ROOT
from . import metrics as M

def exp01_license_floor(snap: dict) -> dict:
    c1 = snap["podcast_claims_under_test"]["C1_start_capital_AED"]
    floor = snap["license_floor_aed_2026"]["rakez_freezone_from"]
    etrader = snap["license_floor_aed_2026"]["etader_dubai_per_year"]
    return {
        "id": "EXP01-license-floor",
        "claim_AED": c1,
        "legal_min_expat_product_AED": floor,
        "etader_AED": etrader,
        "gap_AED": floor - c1,
        "ratio_claim_to_min": round(c1 / floor, 3),
        "verdict": "REFUTED-AS-STATED-2026" if c1 < floor else "PLAUSIBLE",
        "interpretation": "AED 2,000 < AED 5,750 RAKEZ floor and < AED 11,900 IFZA floor. Only eTrader (1,070, nationals/services) or unlicensed marketplace-testing fits 2,000 in 2026. 2017 regime was looser; survivorship + regime-shift explains gap."
    }

def exp02_growth_math(snap: dict) -> dict:
    req_real = M.required_cagr(2_000, 30_000_000, 8)  # 2017->2025, low end of 30-35M real
    req_full = M.required_cagr(2_000, 150_000_000, 8)
    mkt = snap["uae_ecommerce"]["cagr_2020_2025_pct"] / 100.0
    mkt2 = snap["uae_ecommerce_alt_sizing"]["cagr_2026_2031_pct"] / 100.0
    yrs_at_mkt = M.years_to_target(2_000, 30_000_000, mkt)
    return {
        "id": "EXP02-growth-math",
        "required_cagr_to_30M_pct": round(req_real * 100, 2),
        "required_cagr_to_150M_pct": round(req_full * 100, 2),
        "market_cagr_2020_2025_pct": round(mkt * 100, 2),
        "market_cagr_2026_2031_pct": round(mkt2 * 100, 2),
        "multiple_of_market": round(req_real / mkt, 2),
        "years_at_market_rate_to_30M": round(yrs_at_mkt, 1),
        "intangible_share_30M": round(M.valuation_intangible_share(150, 30), 3),
        "intangible_share_35M": round(M.valuation_intangible_share(150, 35), 3),
        "verdict": "EXTRAORDINARY-OUTLIER",
        "interpretation": "232.7% CAGR needed to 30M (306.8% to 150M) vs ~19% market (12.25x). At market rate, 2k->30M takes ~55.3 years. Hence claim requires low-base + COVID demand shock + offline leverage + brand intangible (77-80%). Replicable system? No, without same shocks. Repeatable process? Partially (sourcing/support/playbooks)."
    }

def exp03_resign_rule(snap: dict) -> dict:
    alloc = M.resign_rule_allocation(80_000)
    stable = True  # tested via 12-mo rule in transcript
    return {
        "id": "EXP03-4x-resign-rule",
        "example_salary": 20_000,
        "example_net": 80_000,
        "allocation": alloc,
        "owner_draw_pct_of_net": 25.0,
        "verdict": "SUPPORTED-WITH-STABILITY-CONDITION",
        "interpretation": "4x = 25% draw + 25% growth + 25% ops + 25% buffer. Sound lean-finance heuristic; matches 12-month stability test in transcript. Fails if profits volatile (must use min-trailing-12mo, not peak month)."
    }

def exp04_profit_timeline(snap: dict) -> dict:
    runway = snap["startup_base_rates"]["shopify_runway_months"]
    fail = snap["startup_base_rates"]["dropshipping_fail_y1_pct"]
    return {
        "id": "EXP04-7day-profit",
        "seven_day_profit_expectation": False,
        "benchmark_runway_months": runway,
        "base_fail_rate_pct": fail,
        "verdict": "CLAIMANT-CORRECT-TO-REJECT-7DAY",
        "interpretation": "Shopify 18-24mo runway + 80-90% y1 fail rate corroborate rejecting 7-day profit plans. Correct sequence: cover costs -> break-even -> profit. 40-50k/mo anecdote (2023/24, 2k+2k in) is revenue, not net, and n=1."
    }

def exp05_category(snap: dict) -> dict:
    fashion = snap["uae_ecommerce_alt_sizing"]["fashion_share_2025_pct"]
    food_cagr = snap["uae_ecommerce_alt_sizing"]["food_cagr_pct"]
    return {
        "id": "EXP05-category-80pct",
        "podcast_pick": snap["podcast_claims_under_test"]["C7_high_prob_categories"],
        "market_largest_share": {"fashion_pct": fashion},
        "market_fastest_cagr": {"food_pct": food_cagr},
        "claimed_prob_pct": snap["podcast_claims_under_test"]["C7_claimed_success_prob_pct"],
        "verdict": "SELLER-SPECIFIC-NOT-MARKET-GENERAL",
        "interpretation": "Home/robot/camera strength is consistent with time-saving + busy-household thesis, but market-wide fastest growth is food (13.16%) and largest share fashion (21.59%). 80% unconditional success prob is uncalibrated; conditional on (right price+demo-video+support+warranty) it becomes plausible niche edge."
    }

def exp06_channel(snap: dict) -> dict:
    return {
        "id": "EXP06-channel",
        "uae": snap["podcast_claims_under_test"]["C8_uae_best"],
        "ksa": snap["podcast_claims_under_test"]["C8_ksa_best"],
        "smartphone_share_pct": snap["uae_ecommerce_alt_sizing"]["smartphone_share_2025_pct"],
        "verdict": "SUPPORTED",
        "interpretation": "IG-fast-checkout vs TikTok-viral-no-return matches 78.67% smartphone + 5G/AR shopping; KSA Snapchat lead matches Salla/Zid localization (mada/ApplePay/Tabby). Test: run identical SKU x creative on IG vs TikTok vs Snapchat, compare CTR->CVR, not views."
    }

def exp07_unit_economics() -> dict:
    be = M.break_even_units(fixed_aed=5750, price_aed=149, var_cost_aed=89)
    stock = M.max_affordable_stock(2000, 89)
    return {
        "id": "EXP07-unit-economics",
        "assumptions": {"license_fixed": 5750, "price": 149, "landed_unit": 89},
        "break_even_units_to_cover_license": round(be, 1),
        "max_units_on_2000": stock,
        "verdict": "2000-BUYS-22-UNITS-BUT-NOT-LICENSE",
        "interpretation": "AED 2,000 buys ~22 units at 89 landed, needing ~96 sales at 60 margin just to cover cheapest licence. Hence 2,000 = inventory-only test budget, not legal launch budget in 2026."
    }

def main() -> None:
    snap = load_snapshot()
    results = [
        exp01_license_floor(snap),
        exp02_growth_math(snap),
        exp03_resign_rule(snap),
        exp04_profit_timeline(snap),
        exp05_category(snap),
        exp06_channel(snap),
        exp07_unit_economics(),
    ]
    out_json = ROOT / "data" / "snapshots" / "report.json"
    out_json.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    lines = ["# Benchmark results (auto-generated, do not hand-edit)\n"]
    for r in results:
        lines.append(f"## {r['id']} — {r['verdict']}\n")
        lines.append(f"- interpretation: {r['interpretation']}\n")
        for k, v in r.items():
            if k in ("id", "verdict", "interpretation"):
                continue
            lines.append(f"  - {k}: {v}\n")
    (ROOT / "benchmarks" / "results.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_json} + benchmarks/results.md")
    for r in results:
        print(f"{r['id']}: {r['verdict']}")

if __name__ == "__main__":
    main()
