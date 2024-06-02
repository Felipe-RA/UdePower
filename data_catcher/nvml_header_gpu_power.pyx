from libc.stdint cimport uint32_t
from libc.stdio cimport printf
cdef extern from "nvml.h":
    int nvmlInit()
    int nvmlDeviceGetHandleByIndex(uint32_t index, void** device)
    int nvmlDeviceGetPowerUsage(void* device, uint32_t* power)
    int nvmlShutdown()

def get_gpu_power():
    if nvmlInit() != 0:
        return "Failed to initialize NVML"

    cdef void* device
    cdef uint32_t power_usage

    if nvmlDeviceGetHandleByIndex(0, &device) != 0:
        return "Failed to get device handle"

    if nvmlDeviceGetPowerUsage(device, &power_usage) != 0:
        return "Failed to get power usage"

    nvmlShutdown()
    return f"Power Usage: {power_usage} mW"
