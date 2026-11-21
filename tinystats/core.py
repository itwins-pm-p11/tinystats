import math


def mean(xs):
    xs = list(xs)
    if not xs:
        raise ValueError("mean of empty data")
    return sum(xs) / len(xs)


def median(xs):
    xs = sorted(xs)
    if not xs:
        raise ValueError("median of empty data")
    n = len(xs)
    mid = n // 2
    # BUG: even-length data should average the two middle values
    return xs[mid]


def mode(xs):
    """Return the most common value; ties go to the value seen first."""
    counts = {}
    for x in xs:
        counts[x] = counts.get(x, 0) + 1
    if not counts:
        raise ValueError("mode of empty data")
    # max() returns the first maximal item, and dicts preserve insertion order.
    return max(counts, key=counts.get)


def variance(xs, ddof=1):
    xs = list(xs)
    if len(xs) <= ddof:
        raise ValueError("not enough data")
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - ddof)


def stdev(xs, ddof=1):
    return math.sqrt(variance(xs, ddof))
