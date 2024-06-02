# Importing the necessary C functions
cdef extern from "rocm_smi/rocm_smi.h":
    int rsmi_init(int flags)
    int rsmi_num_monitor_devices(unsigned int *num_devices)
    int rsmi_dev_id_get(unsigned int dv_ind, unsigned long *id)
    int rsmi_dev_name_get(unsigned int dv_ind, char *name, unsigned int len)
    int rsmi_shutdown()

def get_gpu_info():
    cdef unsigned int num_devices = 0
    cdef unsigned long dev_id
    cdef char name[100]
    
    # Initialize ROCm SMI
    if rsmi_init(0) != 0:
        raise Exception("Failed to initialize ROCm SMI")
    
    # Get the number of GPU devices
    if rsmi_num_monitor_devices(&num_devices) != 0 or num_devices == 0:
        raise Exception("Failed to get number of devices or no devices found")
    
    # Gather information from all GPUs
    results = []
    for i in range(num_devices):
        if rsmi_dev_id_get(i, &dev_id) != 0 or rsmi_dev_name_get(i, name, 100) != 0:
            continue  # Skip if there's an error getting data for this device
        results.append((dev_id, name.decode("utf-8")))
    
    # Shutdown ROCm SMI
    rsmi_shutdown()

    return results