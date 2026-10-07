"""Capture real browser screenshots of docs/preview.html.
Usage: python scripts/capture.py  (requires: pip install playwright && playwright install chromium)
Outputs: docs/assets/preview-top.png, docs/assets/preview-quiz.png
Fallback: if playwright missing, keeps existing files (CI still green).
"""
from pathlib import Path
import threading, http.server, functools

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ASSETS = DOCS / "assets"

def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DOCS))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 8901), h)
    httpd.serve_forever()

if __name__ == "__main__":
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print(f"playwright not installed, skipping capture ({e})")
        raise SystemExit(0)
    t = threading.Thread(target=serve, daemon=True)
    t.start()
    import time
    time.sleep(1.0)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1280, "height": 900})
        pg.goto("http://127.0.0.1:8901/preview.html", wait_until="networkidle")
        pg.wait_for_timeout(800)
        pg.screenshot(path=str(ASSETS / "preview-top.png"), full_page=False)
        pg.evaluate("document.querySelector('#quiz').scrollIntoView()")
        pg.wait_for_timeout(600)
        pg.screenshot(path=str(ASSETS / "preview-quiz.png"), full_page=False)
        b.close()
    print("captured preview-top.png + preview-quiz.png")
