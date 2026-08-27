"""
Mann-Kendall Trend Test and Sen's Slope Estimator.
Pure NumPy and SciPy statistical implementation.
"""

from dataclasses import dataclass
from typing import Optional, Union, Sequence
import numpy as np
from scipy import stats

@dataclass(frozen=True)
class MannKendallResult:
    trend: str
    h: bool
    p: float
    z: float
    s: float
    var_s: float
    slope: float
    intercept: float

def mann_kendall(
    data: Union[Sequence[float], np.ndarray],
    alpha: float = 0.05
) -> MannKendallResult:
    """
    Perform non-parametric Mann-Kendall test for monotonic trends.
    """
    x = np.asarray(data, dtype=float)
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 3:
        raise ValueError("Mann-Kendall test requires at least 3 valid observations.")

    s = 0
    for k in range(n - 1):
        s += np.sum(np.sign(x[k + 1 :] - x[k]))

    # Variance calculation with tie handling
    unique, counts = np.unique(x, return_counts=True)
    ties = counts[counts > 1]
    var_s = (n * (n - 1) * (2 * n + 5) - np.sum(ties * (ties - 1) * (2 * ties + 5))) / 18.0

    if s > 0:
        z = (s - 1) / np.sqrt(var_s)
    elif s < 0:
        z = (s + 1) / np.sqrt(var_s)
    else:
        z = 0.0

    p = 2 * (1 - stats.norm.cdf(abs(z)))
    h = p < alpha

    # Sen's slope
    slopes = []
    for i in range(n - 1):
        slopes.extend((x[i + 1 :] - x[i]) / np.arange(1, n - i))
    slope = float(np.median(slopes))
    intercept = float(np.median(x - slope * np.arange(n)))

    if h and slope > 0:
        trend = "increasing"
    elif h and slope < 0:
        trend = "decreasing"
    else:
        trend = "no trend"

    return MannKendallResult(
        trend=trend, h=h, p=float(p), z=float(z), s=float(s), var_s=float(var_s), slope=slope, intercept=intercept
    )
