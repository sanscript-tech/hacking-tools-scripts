# Linux Keylogger
Keyloggers are a type of monitoring software designed to record keystrokes made by a user. One of the oldest forms of cyber threat, these keystroke loggers record the information you type into a website or application and send to back to a third party.

## Executing script
* Install dependencies `pip install -r requirements.txt`
* Execute `python logger.py` to execute the script. Once every 30 seconds the keystrokes will be logged to a file named `key_log.txt`.

## Output

Sample keylog:

```text
[START OF LOGS]
  *~ Date/Time: Mon Oct 26 01:40:16 2020
  *~ User-Profile: User

[SHIFT]Entering [SHIFT]Usernae[BACKSPACE]me [SHIFT]Password. [SHIFT]Hellow [BACKSPACE][BACKSPACE] world [SUPER][SUPER][BACKSPACE][BACKSPACE][BACKSPACE][BACKSPACE][BACKSPACE][BACKSPACE] m

 *~ Date/Time: Mon Oct 26 01:40:46 2020

[ALT][TAB] [SHIFT]Testn[BACKSPACE]ing second half og the log[LEFT ARROW][LEFT ARROW][LEFT ARROW][LEFT ARROW][LEFT ARROW][LEFT ARROW][LEFT ARROW][LEFT ARROW][BACKSPACE]fKey.end oops[ALT][TAB]
```
