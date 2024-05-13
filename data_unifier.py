data_elements = [
    "device_address",  # Bluetooth address of each discovered device
    "device_name",  # Name of the Bluetooth device
    "signal_strength",  # RSSI value indicating the signal strength of the connection
    "tx_power",  # Transmission power level
    "device_power_usage",  # Power usage of each detected device
    "cpu_power_state",  # Power states of the CPU, including active and idle times
    "gpu_power_usage",  # Power usage of the GPU
    "display_backlight_power",  # Power consumption by the display backlight
    "idle_stats",  # System idle statistics to see power saving effectiveness
    "frequency_stats",  # CPU frequency statistics and how often each frequency is used
    "wakeups_per_sec",  # Number of wakeup events per second caused by each component
    "battery_discharge_rate",  # Rate at which battery is discharging
    "energy_consumed",  # Energy consumed by the device over a time period
    "software_activity_impact",  # Impact of software activities on power consumption
    "package_power_state",  # Power states of the entire CPU/GPU package
    "estimated_power_savings",  # Estimated power savings if optimizations are applied
    "thermal_power_management",  # Information on thermal throttling
    "disk_io_power_usage",  # Power usage related to disk I/O operations
    "wireless_radio_power_usage",  # Power consumption by wireless radios
    "power_usage_trends",  # Trends in power usage over the monitoring period
    "system_base_power",  # Baseline power usage when the system is idle
    "wakeups_from_idle",  # Wakeups from idle mode triggered by various components
    "average_cpu_frequency",  # Average CPU frequency over the monitoring period
    "network_latency",  # Network latency measurements, relevant for network performance analysis
    "gpu_core_clock",  # GPU core clock frequency
    "gpu_memory_clock",  # GPU memory clock frequency
    "gpu_temperature",  # Temperature of the GPU
    "gpu_power_limit",  # Power limit for the GPU
    "gpu_utilization",  # GPU utilization percentage
    "gpu_memory_utilization",  # GPU memory utilization percentage
    "cpu_core_clock_avg",  # CPU core clock frequency avgd over all cores
    "cpu_temperature",  # Temperature of the CPU
    "cpu_power_limit",  # Power limit for the CPU
    "cpu_utilization_avg",  # CPU utilization percentage avgd over all cores
    "ram_voltage",  # Voltage of the RAM (mV)
    "ram_frequency",  # Frequency of the RAM (mhz)
    "ram_utilization",  # RAM utilization percentage
    "ram_cas_latency_cl",  # RAM CAS latency with its cl rating
]
