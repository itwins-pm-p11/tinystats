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
    if n % 2 == 0:
        return (xs[mid - 1] + xs[mid]) / 2
    return xs[mid]


def variance(xs, ddof=1):
    xs = list(xs)
    if len(xs) <= ddof:
        raise ValueError("not enough data")
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - ddof)


def stdev(xs, ddof=1):
    return math.sqrt(variance(xs, ddof))
