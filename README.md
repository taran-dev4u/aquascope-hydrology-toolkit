# AquaScope — Scientific Hydrology, Flood Frequency & Time-Series Analytics

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Scientific Computing](https://img.shields.io/badge/SciPy-EVT%20%7C%20GEV%20%7C%20LP3-teal.svg)](https://scipy.org/)
[![Open Source](https://img.shields.io/badge/Open%20Source-9%20Merged%20PRs-green.svg)](https://github.com/Rekin226/aquascope)
[![Pyodide](https://img.shields.io/badge/WebAssembly-Pyodide%20%2F%20WebMCP-orange.svg)](https://pyodide.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit%20Analytics-red.svg)](https://streamlit.io/)

---

## 📌 Executive Summary & Open Source Contributions

**AquaScope** is an open-source scientific hydrology analytics platform providing statistical flood frequency modeling (Extreme Value Theory), hydrological signatures, drought index calculation (SGI), and multi-agency river sensor data ingestion (USGS, UK Environment Agency, Australian BOM, Zenodo GEMStat, CAMELS-BR).

This repository showcases **9 Upstream Merged Contributions** authored by **Taran Mamidala** to the primary open-source codebase ([`Rekin226/aquascope`](https://github.com/Rekin226/aquascope)).

---

## 🚀 Key Upstream Engineering Contributions

### 1. Extreme Value Theory (EVT) GEV Bootstrap Discard Tracking & Formatting ([PR #294](https://github.com/Rekin226/aquascope/pull/294))
- Enhanced Generalized Extreme Value (GEV) distribution fitting by tracking and surfacing filtered-out bootstrap resamples violating shape parameter bounds ($|c| \le 0.50$).
- Threaded discard counts through Python APIs, MCP server, and WebAssembly Pyodide Explorer with threshold caveats.
- Created unified p-value formatting standard ($< 0.001$ floor) eliminating misleading raw zero reporting.

### 2. Australian Bureau of Meteorology (BOM) KiWIS API Resilience ([PR #292](https://github.com/Rekin226/aquascope/pull/292))
- Resolved silent catalog truncation on BOM KiWIS API HTTP 500 errors by raising diagnostic exceptions on total failure and logging structured degradation warnings on partial parameter outages.

### 3. USGS Stage Gage Height Normalization ([PR #269](https://github.com/Rekin226/aquascope/pull/269))
- Fixed critical schema normalization mapping USGS parameter code `00065` (gage height) to `WaterLevelReading` in metric meters and resolved Python 3.10 ISO 8601 trailing `Z` datetime parsing bugs.

### 4. GEMStat Collector Zenodo Cache Protection ([PR #300](https://github.com/Rekin226/aquascope/pull/300))
- Fixed persistent cache poisoning on Zenodo HTML fallbacks by streaming downloads to atomic `.tmp` files, validating non-HTML content headers and `PK` magic bytes, and auto-purging corrupt cache files on failure.

---

## 📂 Repository Structure

```
aquascope-hydrology-toolkit/
├── src/aquascope/
│   ├── hydrology/                   # Flood frequency, GEV/LP3 fitting, and baseflow
│   ├── collectors/                  # Multi-agency API connectors (USGS, BOM, EA, GEMStat)
│   ├── dashboard/                   # Streamlit analytics dashboards
│   └── mcp_server.py                # Model Context Protocol (MCP) server
├── tests/                           # Extensive pytest unit test suite (500+ tests)
└── README.md                        # Documentation
```

---

## 👨‍💻 Author & Contributor
- **Author:** Taran Mamidala
- **Upstream Repository:** [Rekin226/aquascope](https://github.com/Rekin226/aquascope)
