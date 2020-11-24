import sys
import psutil

# Helper method to convert seconds to hours.
def secs_to_hours(secs):
    mm, ss = secs//60, secs%60
    hh, mm = mm//60, mm%60
    return "%d:%02d:%02d" % (hh, mm, ss)

# Check if the OS is supported or not.
if not hasattr(psutil, "sensors_battery"):
    sys.exit("platform not supported")

# Create battery instance.
batt = psutil.sensors_battery()

# Check if battery is installed or not.
if batt is None:
    sys.exit("no battery is installed")

# Print the current battery charge.
print(f"charge:     {round(batt.percent, 2)}")

# Check if battery is plugged in or not.
if batt.power_plugged:
    print(f"status:     {'charging' if batt.percent < 100 else 'fully charged'}")
    print("plugged in: yes")
else:
    print(f"left:       {secs_to_hours(batt.secsleft)}")
    print(f"status:     discharging")
    print(f"plugged in: no")
