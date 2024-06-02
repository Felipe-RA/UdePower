import sys
sys.path.append('build/lib.linux-x86_64-cpython-312')
import rocm_smi_gpu_power

# Use the module
print("Alive: ", type(rocm_smi_gpu_power))
