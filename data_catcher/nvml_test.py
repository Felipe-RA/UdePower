import sys
sys.path.append('build/lib.linux-x86_64-cpython-312')
import nvml_header_gpu_power

# Use the module
print("Alive: ", type(nvml_header_gpu_power))
