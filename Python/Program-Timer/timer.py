import subprocess
import time
import sys

# Check if user has provided commandline arguments or not.
if len(sys.argv) > 1:
    target_prog_params = sys.argv[1:]
else:
    print("Target program not specified...")

# Generate the command to run the script from commandline.
command = ["python"] + target_prog_params

print("Target Output:\n")

# Calculate the time taken to execute the script.
initial_time = time.time()
status = subprocess.call(command)
time_taken = round(time.time() - initial_time, 3)

# Print the time taken to execute the script and the user know if the execution was
# successful or not.
if status == 0:
    print("\033[92m"+f"\n{sys.argv[1]} took {time_taken} seconds to execute successfully."+"\033[0m")
else:
    print("\033[91m"+f"\n{sys.argv[1]} took {time_taken} seconds before failing."+"\033[0m")
