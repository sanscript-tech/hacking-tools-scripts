#import Requried libraries
from time import ctime
from tkinter import *
from threading import *

#time
def cTime():
    while(True):
        c=ctime()
        c=c.split()
        # configure the time 
        lbl.config(text = c[3])

#Creating GUI
main = Tk()

#Title
main.title('Clock')

#lable to show Time
lbl = Label(main, font = ('calibri', 40, 'bold'),background = 'Black', foreground = 'white') 
lbl.pack(anchor = 'center')

#Create new thread
thread=Thread(target=cTime)
thread.start()

main.mainloop()