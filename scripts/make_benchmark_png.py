"""Generate docs/assets/benchmark.png from report.json (no hand drawing)."""
from pathlib import Path
import json
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAS = True
except Exception:
    HAS = False

ROOT = Path(__file__).resolve().parents[1]
rep = json.loads((ROOT / "data" / "snapshots" / "report.json").read_text())
exp02 = next(r for r in rep if r["id"] == "EXP02-growth-math")
vals = {
    "To 30M": exp02["required_cagr_to_30M_pct"],
    "To 150M": exp02["required_cagr_to_150M_pct"],
    "Market": exp02["market_cagr_2020_2025_pct"],
}
out = ROOT / "docs" / "assets" / "benchmark.png"
out.parent.mkdir(parents=True, exist_ok=True)
if HAS:
    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.bar(list(vals.keys()), list(vals.values()))
    ax.set_ylabel("% per year")
    ax.set_title("Required growth vs market (computed)")
    for k, v in vals.items():
        ax.text(list(vals.keys()).index(k), v + 3, f"{v}%", ha="center", fontsize=9)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print(f"wrote {out}")
else:
    # minimal 1x1 png fallback
    import base64
    px = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")
    out.write_bytes(px)
    print(f"wrote fallback {out}")
