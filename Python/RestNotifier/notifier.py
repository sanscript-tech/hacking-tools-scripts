import webbrowser
import time


breaks = int(input("How many breaks do you wish to take? :)"))
break_count = 0
break_time=int(input("Enter after how much time you want a break in seconds(1 hour = 3600s)"))
if(break_count<breaks):
    time.sleep(break_time)
    webbrowser.open("https://www.youtube.com/watch?v=Pw3mhrf7Uuo")
    break_count = break_count+1

if(break_count==1):
    while(break_count<breaks):
        time.sleep(break_time)
        webbrowser.open("https://www.youtube.com/watch?v=Pw3mhrf7Uuo")
        break_count = break_count+1


else:
    exit
