import subprocess
import re

def gather_system_data(polling_rate=3):
    """
    Gathers comprehensive system data including Bluetooth details, power usage metrics, and network analysis,
    utilizing tools like hcitool, powertop, and tshark.

    Parameters:
    - polling_rate: int, defines how frequently to collect data.

    Returns:
    - dict: A dictionary containing detailed metrics about system performance and usage.
    """
    data_dict = {}

    # Execute hcitool to scan for Bluetooth devices
    hcitool_output = subprocess.run(['hcitool', 'scan'], capture_output=True, text=True).stdout.splitlines()
    for line in hcitool_output[1:]:
        if line.strip():
            parts = line.split()
            address, name = parts[0], ' '.join(parts[1:])
            data_dict["device_address"] = address
            data_dict["device_name"] = name
            # Collecting RSSI value for each device
            rssi_output = subprocess.run(['hcitool', 'rssi', address], capture_output=True, text=True).stdout.strip()
            data_dict["signal_strength"] = rssi_output.split()[-1]
            # Collecting transmission power
            tx_power_output = subprocess.run(['hcitool', 'tpl', address], capture_output=True, text=True).stdout.strip()
            data_dict["tx_power"] = tx_power_output.split()[-1]

    # Execute powertop to gather power consumption data
    subprocess.run(['powertop', '--csv=powertop_output.csv', '--time', str(polling_rate)], capture_output=True)
    with open('powertop_output.csv', 'r') as file:
        powertop_data = file.readlines()

    for line in powertop_data:
        if "Device Power Report" in line:
            parts = line.split(',')
            device_name = parts[1].strip()
            power_usage = float(parts[2].strip().split()[0])  # power usage in watts
            data_dict[f"{device_name}_power_usage"] = power_usage
        elif "CPU Power State" in line:
            data_dict["cpu_power_state"] = line.split(',')[2].strip()
        elif "GPU Power Usage" in line:
            data_dict["gpu_power_usage"] = line.split(',')[2].strip()
        elif "Display Backlight Power" in line:
            data_dict["display_backlight_power"] = line.split(',')[2].strip()
        elif "Idle Stats" in line:
            data_dict["idle_stats"] = line.split(',')[2].strip()
        elif "Frequency Stats" in line:
            data_dict["frequency_stats"] = line.split(',')[2].strip()
        elif "Wakeups Per Second" in line:
            data_dict["wakeups_per_sec"] = line.split(',')[2].strip()
        elif "Battery Discharge Rate" in line:
            data_dict["battery_discharge_rate"] = line.split(',')[2].strip()
        elif "Energy Consumed" in line:
            data_dict["energy_consumed"] = line.split(',')[2].strip()
        elif "Software Activity Impact" in line:
            data_dict["software_activity_impact"] = line.split(',')[2].strip()
        elif "Package Power State" in line:
            data_dict["package_power_state"] = line.split(',')[2].strip()
        elif "Estimated Power Savings" in line:
            data_dict["estimated_power_savings"] = line.split(',')[2].strip()
        elif "Thermal Power Management" in line:
            data_dict["thermal_power_management"] = line.split(',')[2].strip()
        elif "Disk IO Power Usage" in line:
            data_dict["disk_io_power_usage"] = line.split(',')[2].strip()
        elif "Wireless Radio Power Usage" in line:
            data_dict["wireless_radio_power_usage"] = line.split(',')[2].strip()
        elif "Power Usage Trends" in line:
            data_dict["power_usage_trends"] = line.split(',')[2].strip()
        elif "System Base Power" in line:
            data_dict["system_base_power"] = line.split(',')[2].strip()
        elif "Wakeups From Idle" in line:
            data_dict["wakeups_from_idle"] = line.split(',')[2].strip()

    # Using tshark to monitor network traffic
    tshark_command = ['tshark', '-a', f'duration:{polling_rate * 10}', '-w', 'network_traffic.pcap']
    subprocess.run(tshark_command, capture_output=True)
    read_command = ['tshark', '-r', 'network_traffic.pcap', '-T', 'fields', '-e', 'frame.time_epoch', '-e', 'ip.src', '-e', 'ip.dst', '-e', 'frame.len']
    tshark_output = subprocess.run(read_command, capture_output=True, text=True).stdout.splitlines()

    # Extracting and processing network data from tshark output
    for line in tshark_output:
        if line:
            epoch_time, src_ip, dst_ip, frame_length = line.split()
            data_dict[f"{epoch_time}_network_traffic_src_{src_ip}_dst_{dst_ip}"] = frame_length
            # frame_length reflects network latency in milliseconds
            data_dict["network_latency"] = float(frame_length) / 1000

    return data_dict

# Example usage
if __name__ == "__main__":
    system_data = gather_system_data()
    print(system_data)
