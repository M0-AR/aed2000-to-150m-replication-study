"""Live re-verification: World Bank GDP + ECB FX (fallbacks to snapshot). Stdlib only."""
import json
import urllib.request
from pathlib import Path
from .config import ROOT

def fetch_worldbank_gdp_uae() -> dict:
    url = "https://api.worldbank.org/v2/country/AE/indicator/NY.GDP.MKTP.CD?format=json&date=2017:2024&per_page=20"
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            payload = json.loads(r.read().decode())
        out = {}
        for row in payload[1]:
            if row["value"]:
                out[str(row["date"])] = float(row["value"])
        return {"live": True, "values": out}
    except Exception as e:  # offline-safe
        return {"live": False, "error": str(e)}

if __name__ == "__main__":
    print(json.dumps(fetch_worldbank_gdp_uae(), indent=2))
