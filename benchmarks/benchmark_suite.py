"""Benchmark matrix: each podcast claim vs public market anchor.
Run: python -m benchmarks.benchmark_suite  (stdlib only)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAP = json.loads((ROOT / "data" / "snapshots" / "market_2026.json").read_text(encoding="utf-8"))

ROWS = [
    ("C1 2k start", "AED 5,750 RAKEZ floor; 1,070 eTrader nationals-only", "REFUTED-AS-STATED-2026", "Regime shift since 2017"),
    ("C2 2k->150M", "129% CAGR needed vs 19% market; 56y at market rate", "EXTRAORDINARY-OUTLIER", "Low-base + COVID + offline + intangible"),
    ("C3 4x resign", "25/25/25/25 + 12-mo stability", "SUPPORTED-CONDITIONAL", "Use trailing-min, not peak"),
    ("C4 no 7-day profit", "Shopify 18-24mo; 80-90% y1 fail", "SUPPORTED", "Cover-costs-first sequence"),
    ("C5 copy+innovate", "Feindt02; Luo24 resource-constrained scaling", "SUPPORTED", "Support/warranty = moat"),
    ("C6 emotion>specs", "Apple-color/battery-hours vs mAh spec", "SUPPORTED", "Demo-video > spec-sheet"),
    ("C7 home/robot/cam 80%", "Fashion 21.59% share; food 13.16% CAGR fastest", "SELLER-SPECIFIC", "Needs calibration"),
    ("C8 IG/TT vs Snap", "Smartphone 78.67%; Salla/Zid KSA", "SUPPORTED", "Test CTR->CVR per channel"),
    ("C9 offline 50/50", "Mall expansion + tactile buyer + attach-selling", "PLAUSIBLE", "Close/move, never just close"),
    ("C10 organic>paid", "IG paid-opt-out update; influencer discount depth", "PLAUSIBLE-2026", "Hook+short+proof"),
    ("C11 AI inv/voice/pers", "Narrow/Business AI; forecast+alerts", "SUPPORTED-DIRECTIONAL", "Measure hrs saved + stockout delta"),
    ("C12 COVID at-cost", "GDP -17.7% 19-20; e-com +19% CAGR", "SUPPORTED-AS-CAC", "At-cost = acquisition spend"),
]

if __name__ == "__main__":
    print(f"{'claim':<22} | {'anchor':<52} | verdict")
    print("-" * 110)
    for c, a, v, n in ROWS:
        print(f"{c:<22} | {a:<52} | {v} ({n})")
