"""Benchmark for vectorized Mann-Kendall trend calculation."""
import time
import numpy as np
from aquascope_toolkit.trends import mann_kendall

def bench():
    series = np.random.randn(500)
    start = time.perf_counter()
    for _ in range(100):
        mann_kendall(series)
    print(f"500-point MK test x100: {(time.perf_counter()-start)*1000:.2f}ms")

if __name__ == "__main__":
    bench()
