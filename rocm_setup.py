from setuptools import setup
from Cython.Build import cythonize

setup(
    name="GPU Info",
    ext_modules=cythonize("rocm_smi_gpu_power.pyx"),
    include_dirs=["/opt/rocm/include"],
    library_dirs=["/opt/rocm/lib"],
    libraries=["rocm_smi64"]  # change if your installation is different 
)
