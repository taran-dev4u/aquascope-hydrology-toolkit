# AquaScope — Scientific Hydrology Toolkit Contributions

Repository showcasing 9 upstream merged contributions to the open-source **AquaScope** hydrology platform ([Rekin226/aquascope](https://github.com/Rekin226/aquascope)).

## Key Contributions

- **GEV Bootstrap Discard Tracking (PR #294):** Surfaced filtered-out resamples violating shape parameter bounds ($|c| \le 0.50$) in Generalized Extreme Value distribution fitting and standardized p-value formatting with a $< 0.001$ floor.
- **BOM KiWIS API Resilience (PR #292):** Handled HTTP 500 errors gracefully with partial degradation logging.
- **USGS Normalization (PR #269):** Normalized gage height parameter codes to `WaterLevelReading` and fixed Python 3.10 ISO 8601 trailing `Z` datetime parsing.
- **Zenodo Cache Protection (PR #300):** Added atomic `.tmp` download streaming, magic byte verification, and automatic corrupt cache purging.
