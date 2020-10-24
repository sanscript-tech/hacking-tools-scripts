import psutil
import notify2
import time
import sys

if len(sys.argv) > 1:
    THRESHOLD = float(sys.argv[1])
else:
    print("Please provide threshold limit...")
    sys.exit()

APP_NAME = "Network Usage Notifier"
APP_DESC = f"You will be notified when your network usage exceeds {THRESHOLD}MB"
APP_ICON = "icon.png"
NOTIF_TITLE = "NETWORK USAGE EXCEEDED!!"
NOTIF_DESC = f"Network usage exceeded {THRESHOLD}MB"

net_counter = psutil.net_io_counters()
initial_usage = net_counter.bytes_sent + net_counter.bytes_recv

notify2.init(APP_NAME)
notification = notify2.Notification(APP_NAME, APP_DESC, APP_ICON)
notification.set_timeout(5000)
notification.show()

while True:
    net_counter = psutil.net_io_counters()
    current_usage = net_counter.bytes_sent + net_counter.bytes_recv
    delta_usage = current_usage - initial_usage

    if delta_usage/1e+6 >= THRESHOLD:
        notification.set_urgency(notify2.URGENCY_CRITICAL)
        notification.update(NOTIF_TITLE, NOTIF_DESC)
        notification.show()

        initial_usage = current_usage

    time.sleep(5)
