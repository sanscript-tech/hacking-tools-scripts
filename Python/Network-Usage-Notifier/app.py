import psutil
import time
import sys

# Check if the operating system is windows or not.
IS_WINDOWS = sys.platform == 'windows'

# Check if the user has provided the THRESHOLD or not
if len(sys.argv) > 1:
    THRESHOLD = float(sys.argv[1])
else:
    print("Please provide threshold limit...")
    sys.exit()

# Constants to provide notification information.
APP_NAME = "Network Usage Notifier"
APP_DESC = f"You will be notified when your network usage exceeds {THRESHOLD}MB"
APP_ICON = "images/icon.png"
NOTIF_TITLE = "NETWORK USAGE EXCEEDED!!"
NOTIF_DESC = f"Network usage exceeded {THRESHOLD}MB"

# Calculate the initial network usage.
net_counter = psutil.net_io_counters()
initial_usage = net_counter.bytes_sent + net_counter.bytes_recv

# Initialize notifications.
if IS_WINDOWS:
    import win10toast
    notification = win10toast.ToastNotifier()
else:
    import notify2
    notify2.init(APP_NAME)
    notification = notify2.Notification(APP_NAME, APP_DESC, APP_ICON)
    notification.set_timeout(5000)
    notification.show()

# Event loop to check for usage.
while True:
    # Calculate the change in network usage
    net_counter = psutil.net_io_counters()
    current_usage = net_counter.bytes_sent + net_counter.bytes_recv
    delta_usage = current_usage - initial_usage

    # Check if usage exceeds THRESHOLD
    if delta_usage/1e+6 >= THRESHOLD:
        # Show notification
        if IS_WINDOWS:
            notification.show_toast(NOTIF_TITLE, NOTIF_DESC, APP_ICON, 5, True)
        else:
            notification.set_urgency(notify2.URGENCY_CRITICAL)
            notification.update(NOTIF_TITLE, NOTIF_DESC)
            notification.show()

        # Resey initial network usage.
        initial_usage = current_usage

    # Sleep for 5 seconds to save system resources.
    time.sleep(5)
