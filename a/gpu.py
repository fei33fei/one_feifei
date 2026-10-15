import cupy as cp
import numpy as np

# 测试 CuPy
arr_gpu = cp.array([1, 2, 3, 4])
print(f"CuPy works: {arr_gpu * 2}")

# 测试 CUDA
print(f"CUDA available: {cp.cuda.is_available()}")
print(f"CUDA runtime version: {cp.cuda.runtime.runtimeGetVersion()}")