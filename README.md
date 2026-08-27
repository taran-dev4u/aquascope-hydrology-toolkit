# AquaScope — Extreme Value Theory & Hydrology Intelligence Platform

[![CI](https://github.com/taran-dev4u/aquascope-hydrology-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/taran-dev4u/aquascope-hydrology-toolkit/actions/workflows/ci.yml)
[![Upstream PRs](https://img.shields.io/badge/AquaScope-9%20Merged%20PRs-green?logo=github)](https://github.com/Rekin226/aquascope/pulls?q=is%3Apr+author%3Ataran-dev4u)
[![Upstream Stars](https://img.shields.io/badge/Upstream%20Stars-19%2B%20%E2%AD%90-yellow?logo=github)](https://github.com/Rekin226/aquascope)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Hydrological and statistical analysis toolkit supporting [AquaScope](https://github.com/Rekin226/aquascope), an open-source scientific computing platform for global water resources.

---

## 🎯 Upstream Contributions (9 Merged Pull Requests)

1. **Extreme Value Theory Flood Modeling ([PR #154](https://github.com/Rekin226/aquascope/pull/154)):** Seeded MLE GEV fit with L-moments and enforced shape constraint $|c| \le 0.5$, preventing degenerate return-period quantiles on ~40-year records.
2. **Mann-Kendall & Sen's Slope ([PR #147](https://github.com/Rekin226/aquascope/pull/147)):** Shipped vectorized NumPy/SciPy statistical trend detection module with tiebreaker variance correction.
3. **CAMELS-BR Collector ([PR #140](https://github.com/Rekin226/aquascope/pull/140)):** Implemented national catchment collector parsing 897 Brazilian streamflow records into OGC GeoJSON schemas.
4. **CI CHANGELOG Enforcement ([PR #150](https://github.com/Rekin226/aquascope/pull/150)):** Standalone GitHub Actions CI workflow enforcing changelog entries with unit test guards.
5. **Flow Duration Curve Slope ([PR #148](https://github.com/Rekin226/aquascope/pull/148)):** Log-space percentile slope and standalone runoff ratio signatures.
6. **Dashboard Live Sources ([PR #145](https://github.com/Rekin226/aquascope/pull/145)):** Wired all 25 live data sources into interactive Streamlit interface with automated drift protection.

---

## 📄 License

Licensed under the [MIT License](LICENSE).
