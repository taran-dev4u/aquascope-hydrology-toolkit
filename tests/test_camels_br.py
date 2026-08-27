"""Unit tests for CAMELS-BR collector."""
import unittest
from aquascope_toolkit.collectors.camels_br import CAMELSBRCollector

class TestCAMELSBR(unittest.TestCase):
    def test_catchment_count(self):
        c = CAMELSBRCollector()
        self.assertEqual(c.get_metadata()["catchments"], 897)
