import subprocess
import time

def run_uprof(polling_rate=3):
    """
    Runs AMD uProf to collect performance and power data at a defined polling rate.

    Parameters:
    - polling_rate: int, the interval in seconds at which data is sampled (default: 3 seconds).

    The function starts the uProf profiling session, collects data for the specified duration,
    then stops the profiling and generates a report.
    """
    # Setup configuration for uProf (adjust the command to match your setup and requirements)
    config_command = f"AMDuProfCLI config --event-based-sampling --polling-interval {polling_rate}"
    subprocess.run(config_command, shell=True)

    # Start the profiling session
    start_command = "AMDuProfCLI start --config my_profile_config.uprof"
    subprocess.run(start_command, shell=True)

    # Let it collect data for the specified polling_rate
    time.sleep(polling_rate)

    # Stop the profiling session
    stop_command = "AMDuProfCLI stop"
    subprocess.run(stop_command, shell=True)

    # Retrieve and process the report
    report_command = "AMDuProfCLI report --session my_session_name --reportpath ./report.csv"
    subprocess.run(report_command, shell=True)

def read_and_process_report(report_path='report.csv'):
    """
    Reads and processes the profiling report generated by AMD uProf.

    Parameters:
    - report_path: str, the path to the report file generated by uProf (default: './report.csv').

    The function reads the report data, prints out the average power consumption,
    and can be extended to perform further data analysis.
    """
    import pandas as pd

    # Read the data into a DataFrame
    data = pd.read_csv(report_path)

    # Example analysis: Calculate the average power consumption
    if 'Power' in data.columns:
        average_power = data['Power'].mean()
        print(f"Average Power Consumption: {average_power} Watts")
    else:
        print("Power data not found in the report.")

# Example of running the function
if __name__ == "__main__":
    run_uprof(polling_rate=3)
    read_and_process_report()
