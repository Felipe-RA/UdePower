from setuptools import setup
from Cython.Build import cythonize

setup(
    name="NVIDIA GPU Power Module",
    ext_modules=cythonize("nvml_header_gpu_power.pyx", language_level="3"),
    include_dirs=["headers/"] # where to find nvml.h
)
