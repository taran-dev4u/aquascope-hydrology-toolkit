"""CAMELS-BR Brazilian catchment streamflow data collector."""
from typing import Dict, Any, List

class CAMELSBRCollector:
    """Collector for 897 Brazilian catchments."""
    TOTAL_CATCHMENTS = 897
    
    def get_metadata(self) -> Dict[str, Any]:
        return {
            "source": "CAMELS-BR",
            "country": "Brazil",
            "catchments": self.TOTAL_CATCHMENTS,
            "format": "OGC GeoJSON"
        }
