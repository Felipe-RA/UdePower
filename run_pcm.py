import subprocess
import time

def run_pcm(polling_rate=3):
    """
    Runs Intel PCM to collect CPU and memory performance data at a defined polling rate.

    Parameters:
    - polling_rate: int, the interval in seconds at which data is sampled (default: 3 second).

    This function runs the pcm.x tool, collects output for the specified duration,
    then terminates the tool and saves the output to a text file.
    """
    # Start the PCM tool
    pcm_command = ['./pcm.x', str(polling_rate)]
    pcm_process = subprocess.Popen(pcm_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Let it collect data for the specified duration
    time.sleep(polling_rate)

    # Terminate the process and get the output
    pcm_process.terminate()
    try:
        outs, errs = pcm_process.communicate(timeout=2)
    except subprocess.TimeoutExpired:
        pcm_process.kill()
        outs, errs = pcm_process.communicate()

    # Write output to file
    with open('pcm_output.txt', 'w') as f:
        f.write(outs)
    print("Data collection complete. Output saved to 'pcm_output.txt'.")

def analyze_pcm_output(file_path='pcm_output.txt'):
    """
    Reads and processes the PCM output saved in a text file.

    Parameters:
    - file_path: str, the path to the PCM output file.

    This function reads the PCM output, could parse it, and analyze the data.
    Example here is basic and depends heavily on the output format of PCM.
    """
    with open(file_path, 'r') as file:
        data = file.readlines()
        return data
