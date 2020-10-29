import subprocess  # to open zoom application
import pyautogui   # automate mouse movement and typing
import time 
from datetime import datetime
import pandas as pd
import os


def sign_in(meet_id, password, duration):

    # enter your zoom application path, example is shown
    subprocess.Popen("C:\\Users\\Admin\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

    time.sleep(2)

    # Click join button
    join = pyautogui.locateCenterOnScreen('join_button_img.png')
    pyautogui.moveTo(join)
    pyautogui.click()

    # Type the meeting ID
    meeting_id_btn =  pyautogui.locateCenterOnScreen('meeting_id_btn.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meet_id)

    # Disables both the camera and the mic
    media_btn = pyautogui.locateAllOnScreen('media_btn.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(2)

    # Hits the join button
    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    
    time.sleep(5)

    #Types the password and hits enter
    meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.write(password)
    pyautogui.press('enter')

    #Total time of zoom session
    time.sleep(duration) 

    # closing Zoom
    os.system("TASKKILL /F /IM Zoom.exe")
    time.sleep(0.5)


# Reading the file
df = pd.read_csv('schedule.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]  
       meet_id = str(row.iloc[0,1])  
       meet_paasword = str(row.iloc[0,2])
       duration = str(row.iloc[0,3])

       # calling sign_in funstion and passing requires parameters
       sign_in(meet_id, meet_paasword, duration)
       time.sleep(40)
       print('Signed in, Meeting Started')
       
