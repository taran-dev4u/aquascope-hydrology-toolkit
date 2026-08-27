"""Generalized Extreme Value (GEV) Flood Frequency Distribution Modeling."""
import numpy as np
from scipy import stats
from dataclasses import dataclass

@dataclass
class GEVFitResult:
    c: float  # shape parameter
    loc: float
    scale: float
    method: str

def fit_gev_flood(data: np.ndarray, max_abs_shape: float = 0.5) -> GEVFitResult:
    x = np.asarray(data, dtype=float)
    x = x[~np.isnan(x)]
    if len(x) < 5:
        raise ValueError("GEV fitting requires at least 5 observations")
    c, loc, scale = stats.genextreme.fit(x)
    if abs(c) > max_abs_shape:
        c = np.clip(c, -max_abs_shape, max_abs_shape)
    return GEVFitResult(c=float(c), loc=float(loc), scale=float(scale), method="mle_constrained")
