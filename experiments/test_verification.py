"""Unit tests = verification gate. No file is 'enhanced' without these passing."""
from src import metrics as M

def test_cagr_basic():
    r = M.required_cagr(100, 200, 1)
    assert abs(r - 1.0) < 1e-9

def test_years_to_target():
    y = M.years_to_target(2000, 30000000, 0.19)
    assert 50 < y < 65  # ~56y at 19%

def test_outlier_gap():
    req = M.required_cagr(2000, 30000000, 8)
    assert req > 1.0  # >100%
    assert req / 0.19 > 5  # >5x market

def test_resign_alloc():
    a = M.resign_rule_allocation(80000)
    assert a["salary"] == 20000
    assert sum(a.values()) == 80000

def test_break_even():
    be = M.break_even_units(5750, 149, 89)
    assert 90 < be < 105

def test_intangible():
    assert abs(M.valuation_intangible_share(150, 30) - 0.8) < 1e-9
