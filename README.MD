# Installation and Setup of Binaries

## NVIDIA tools (Maxwell and Higher)

**1. Install de nvidia utils.**

```bash
sudo apt install nvidia-utils-535
```

> **NOTE: For better compatibility, replace the `nvml.h` header within the `headers` folder with the nvml that comes with the drivers of your nvidia gpu.**

**2. Run to generate the `.c file`  and the `shared object [.so] file`**

```bash
python3 nvml_setup.py build_ext
```

## AMD GPU tools  (Polaris and Higher)

**1. Install ROCm (follow the official amd instructions at [the official ROCm Linux distribution center](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/))** 


**2. Check which rocm_smi installation you have running:**

```bash
ls /opt/rocm/lib | grep rocm_smi
```

You should see something similar to this:

```ts
librocm_smi64.so
librocm_smi64.so.5
librocm_smi64.so.5.0.50700
```

<br>

**3. Check if the library is correctly configured with your system paths with:**

```bash
ldconfig -p | grep rocm_smi
```

If correct, you should get something like this as an output:

```ts
librocm_smi64.so.5 (libc6,x86-64) => /opt/rocm-5.7.0/lib/librocm_smi64.so.5
librocm_smi64.so (libc6,x86-64) => /opt/rocm-5.7.0/lib/librocm_smi64.so
```

> **NOTE:** If you find any problems related to missing libraries, a possible fix may be updating the `LD_LIBRARY_PATH` environment variable to include `/opt/rocm/lib`:


```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rocm/lib
```

<br>

**4. Modify the `rocm_setup.py` file if your rocm installation differs from `rocm_smi64`. Like this:**

```python
setup(
    name="GPU Info",
    ext_modules=cythonize("rocm_smi_gpu_power.pyx"),
    include_dirs=["/opt/rocm/include"],
    library_dirs=["/opt/rocm/lib"],
    libraries=["rocm_smi64"]  # change if your installation is different 
)
```

<br>

**5.Generate the `.so` binaries and the `c code` running:**

```bash
python3 rocm_setup.py build_ext
```

You should find the newly created .so object below the `lib.linux-x86_64-cpython-312` folder.

## Installing AMD uProf (CPU's on ZEN2 and upwards)


**1. Install the AMD uProf packages at [the official amd site](https://www.amd.com/es/developer/uprof.html)**

2. Restart your system.


## Installing INTEL PCM (CPU's on ZEN2 and upwards)

**1. Clone the PCM repo with the submodules**

```bash
git clone --recursive https://github.com/intel/pcm.git
```

**2.Install `cmake`**

```bash
mkdir build
cd build
cmake ..
cmake --build .
```

**3.Build the utility.**

```bash
cmake --build . --parallel
```

