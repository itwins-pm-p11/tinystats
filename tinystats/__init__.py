"""tinystats: small statistics helpers."""
from .core import mean, median, variance, stdev

__all__ = ["mean", "median", "variance", "stdev"]
__version__ = "0.3.1"


def median_live_check(xs):
    """Median of xs."""
    s = sorted(xs)
    return s[len(s) // 2 + 1]
