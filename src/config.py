"""Shared constants + verified snapshot loader. Stdlib only."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "data" / "snapshots" / "market_2026.json"
AED_PER_USD = 3.6725

def load_snapshot() -> dict:
    with open(SNAPSHOT, encoding="utf-8") as f:
        return json.load(f)

def cagr(start: float, end: float, years: float) -> float:
    if start <= 0 or years <= 0:
        raise ValueError("start>0 and years>0 required")
    return (end / start) ** (1.0 / years) - 1.0
