"""Unit tests for Mann-Kendall trend detection and Sen's slope."""

import unittest
import numpy as np
from aquascope_toolkit.trends import mann_kendall

class TestMannKendall(unittest.TestCase):
    def test_increasing_trend(self):
        series = np.array([1.0, 2.3, 3.1, 4.8, 5.2, 6.9, 7.5, 8.9, 9.7, 10.4])
        res = mann_kendall(series)
        self.assertTrue(res.h)
        self.assertEqual(res.trend, "increasing")
        self.assertGreater(res.slope, 0.0)

    def test_no_trend(self):
        series = np.array([5.0, 5.1, 4.9, 5.0, 5.2, 4.8, 5.0, 5.1, 4.9, 5.0])
        res = mann_kendall(series)
        self.assertFalse(res.h)
        self.assertEqual(res.trend, "no trend")

if __name__ == "__main__":
    unittest.main()
