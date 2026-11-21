import pytest
import tinystats
from tinystats import mean, median, mode, variance, stdev


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even():
    assert median([4, 1, 3, 2]) == 2.5


def test_variance():
    assert variance([2, 4, 4, 4, 5, 5, 7, 9]) == pytest.approx(4.571428571)


def test_stdev_population():
    assert stdev([2, 4, 4, 4, 5, 5, 7, 9], ddof=0) == pytest.approx(2.0)


def test_empty():
    with pytest.raises(ValueError):
        mean([])


def test_mode():
    assert mode([1, 2, 2, 3]) == 2


def test_mode_single_value():
    assert mode([7]) == 7


def test_mode_tie_returns_smallest():
    assert mode([3, 3, 1, 1, 2]) == 1


def test_mode_all_unique_returns_smallest():
    assert mode([5, 4, 9]) == 4


def test_mode_accepts_iterator():
    assert mode(iter([4, 4, 2])) == 4


def test_mode_empty():
    with pytest.raises(ValueError):
        mode([])


def test_mode_exposed_on_package():
    assert tinystats.mode is mode
    assert "mode" in tinystats.__all__
