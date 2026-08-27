"""Hydrological signatures: FDC slope and Runoff Ratio."""
import numpy as np

def fdc_slope(discharge: np.ndarray, lower: float = 0.33, upper: float = 0.66) -> float:
    q = np.sort(discharge[~np.isnan(discharge)])[::-1]
    n = len(q)
    idx_low = int(lower * n)
    idx_up = int(upper * n)
    q_low = max(q[idx_low], 1e-6)
    q_up = max(q[idx_up], 1e-6)
    return float((np.log(q_low) - np.log(q_up)) / (upper - lower))
