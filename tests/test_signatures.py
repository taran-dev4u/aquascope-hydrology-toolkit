"""Unit tests for hydrological signatures."""
import unittest
import numpy as np
from aquascope_toolkit.signatures import fdc_slope

class TestSignatures(unittest.TestCase):
    def test_fdc_slope_positive(self):
        q = np.linspace(100, 10, 100)
        slope = fdc_slope(q)
        self.assertGreater(slope, 0.0)
