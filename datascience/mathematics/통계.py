from typing import List
from collections import Counter
import math

# fixme import modules for sum_of_squares
from datascience.mathematics.vector import sum_of_squares
from datascience.mathematics.vector import dot

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


def median(v: List[float]) -> float:
    return sorted(v)[len(v) // 2] if len(v) % 2 == 1 else (sorted(v)[len(v) // 2] + sorted(v)[len(v) // 2 - 1]) / 2


assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2


def quantile(xs: List[float], p: float) -> float:
    """Returns the pth-percentile value in x"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


num_friends = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 6, 6]


def mode(x: List[float]) -> List[float]:
    return [m for m in Counter(x).keys() if Counter(x)[m] == max(Counter(x).values())]


assert set(mode(num_friends)) == {1, 6}


def de_mean(xs: List[float]) -> List[float]:  # fixme 평균과의 차이
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def variance(xs: List[float]) -> float:  # fixme 분산
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "variance requires at least two elements"

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    return math.sqrt(variance(xs))


def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and the 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)

def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "sx and ys must have same number of elements"

    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

assert 22.42 < covariance(num_friends, daily_minutes) < 22.43