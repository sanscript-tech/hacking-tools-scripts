import subprocess
import time
import sys

if len(sys.argv) > 1:
    target_prog_params = sys.argv[1:]
else:
    print("Target program not specified...")

command = ["python"] + target_prog_params

print("Target Output:\n")

initial_time = time.time()
status = subprocess.call(command)
time_taken = round(time.time() - initial_time, 3)

if status == 0:
    print(f"\n{sys.argv[1]} took {time_taken} seconds to execute successfully.")
else:
    print(f"\n{sys.argv[1]} took {time_taken} seconds before failing.")