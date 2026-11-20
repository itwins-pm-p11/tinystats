"""tinystats: small statistics helpers."""
from .core import mean, median, variance, stdev

__all__ = ["mean", "median", "variance", "stdev"]
__version__ = "0.3.1"


def variance_live_check(xs):
    """Population variance of xs."""
    m = sum(xs) / len(xs)
    return sum((x - m) for x in xs) / len(xs)
