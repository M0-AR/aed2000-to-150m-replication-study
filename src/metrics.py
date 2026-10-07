"""Core falsifiable metrics. Every formula is unit-tested; no hand edits."""
from __future__ import annotations
import math

def required_cagr(start: float, end: float, years: float) -> float:
    return (end / start) ** (1.0 / years) - 1.0

def years_to_target(start: float, end: float, rate: float) -> float:
    if rate <= 0:
        raise ValueError("rate must be >0")
    return math.log(end / start) / math.log(1.0 + rate)

def max_affordable_stock(capital_aed: float, unit_landed_aed: float) -> int:
    if unit_landed_aed <= 0:
        raise ValueError("unit cost >0")
    return int(capital_aed // unit_landed_aed)

def break_even_units(fixed_aed: float, price_aed: float, var_cost_aed: float) -> float:
    margin = price_aed - var_cost_aed
    if margin <= 0:
        return float("inf")
    return fixed_aed / margin

def resign_rule_allocation(monthly_net: float) -> dict:
    """4x rule: salary + develop + ops-reinvest + buffer, each 1x salary."""
    salary = monthly_net / 4.0
    return {"salary": salary, "develop": salary, "ops_reinvest": salary, "buffer": salary}

def valuation_intangible_share(market_m: float, real_m: float) -> float:
    return (market_m - real_m) / market_m

def verdict(pass_: bool) -> str:
    return "PASS" if pass_ else "FAIL"
