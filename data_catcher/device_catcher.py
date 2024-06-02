import subprocess
import re

def get_system_cpu_gpu():
    """
    Identifies the CPU and GPU model of the system.

    Returns:
    - dict: Dictionary containing the CPU and GPU model names.
    """
    system_info = {}

    # Fetch CPU model
    try:
        cpu_info = subprocess.run(['cat', '/proc/cpuinfo'], capture_output=True, text=True).stdout
        # Use regular expression to find the model name from cpuinfo
        match = re.search(r"model name\t: (.+)", cpu_info)
        if match:
            system_info['cpu'] = match.group(1).strip()
        else:
            system_info['cpu'] = "Unknown CPU Model"
    except Exception as e:
        system_info['cpu'] = f"Failed to determine CPU model: {str(e)}"

    # Fetch GPU model using lshw
    try:
        gpu_info = subprocess.run(['lshw', '-C', 'display'], capture_output=True, text=True).stdout
        # Differentiate between NVIDIA, AMD, and Intel GPUs
        if 'NVIDIA' in gpu_info:
            vendor = "NVIDIA"
        elif 'Advanced Micro Devices' in gpu_info or 'AMD' in gpu_info:
            vendor = "AMD"
        elif 'Intel Corporation' in gpu_info:
            vendor = "Intel"
        else:
            vendor = "Unknown GPU Vendor"

        # Extract GPU model using regular expressions based on the vendor identified
        if vendor != "Unknown GPU Vendor":
            match = re.search(r"description: VGA compatible controller\n\s+product: (.+)\n\s+vendor: " + vendor, gpu_info, re.IGNORECASE)
            if match:
                system_info['gpu'] = f"{vendor} {match.group(1).strip()}"
            else:
                system_info['gpu'] = "Unknown GPU Model"
        else:
            system_info['gpu'] = "Unknown GPU Model"
    except Exception as e:
        system_info['gpu'] = f"Failed to determine GPU model: {str(e)}"

    return system_info

if __name__ == "__main__":
    hardware_info = get_system_cpu_gpu()
    ## when used as a standalone script, print the hardware info
    print(hardware_info)
