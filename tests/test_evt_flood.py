"""Unit tests for GEV flood distribution fitting."""
import unittest
import numpy as np
from aquascope_toolkit.evt_flood import fit_gev_flood

class TestGEVFlood(unittest.TestCase):
    def test_gev_fitting_bounds(self):
        synthetic = np.random.exponential(scale=100.0, size=50)
        res = fit_gev_flood(synthetic, max_abs_shape=0.5)
        self.assertLessEqual(abs(res.c), 0.5)
        self.assertGreater(res.scale, 0.0)
