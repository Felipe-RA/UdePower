import time
import csv
from data_unifier import gather_data as data_unifier_gather
from device_catcher import gather_data as device_catcher_gather
from powertop_hci_extractor import gather_system_data as powertop_hci_gather
from run_pcm import gather_pcm_data
from run_uprof import gather_uprof_data
from nvml_header_gpu_power import gather_nvml_data
from rocm_smi_gpu_power import gather_rocm_data

def run_all_functions(polling_rate=3):
    """
    Runs all the data collection functions imported from various modules,
    collects their outputs, and writes the data to a CSV file.

    Args:
    polling_rate (int): Time in seconds between data polls. Default is 3 seconds.
    """
    # Define the CSV file and the headers based on the data points you expect to collect
    csv_file = 'laptop_stats.csv'
    headers = ['timestamp', 'data_unifier', 'device_catcher', 'powertop_hci', 'pcm_data', 'uprof_data', 'nvml_data', 'rocm_data']

    # Check if the CSV needs headers
    try:
        with open(csv_file, 'x', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
    except FileExistsError:
        pass

    # Collect data every 'polling_rate' seconds
    start_time = time.time()
    while time.time() - start_time < polling_rate:
        # Run each function and store the results
        results = {
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'data_unifier': data_unifier_gather(),
            'device_catcher': device_catcher_gather(),
            'powertop_hci': powertop_hci_gather(),
            'pcm_data': gather_pcm_data(),
            'uprof_data': gather_uprof_data(),
            'nvml_data': gather_nvml_data(),
            'rocm_data': gather_rocm_data()
        }

        # Write results to the CSV file
        with open(csv_file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerow(results)

        # Wait for the next cycle
        time.sleep(polling_rate)

if __name__ == "__main__":
    run_all_functions()
