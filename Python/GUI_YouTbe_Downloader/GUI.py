from tkinter.ttk import *
from pytube import * 
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
global itaglist
itaglist=[]

def progress(stream=None,chunk=None,remaining=None):
    file_downloaded=(file_size - remaining)
    per=(file_downloaded / file_size) * 100
    downloadButton.config(text="{:00.0f} % downloaded".format(per))
    progressBar['value']=per
    main.update_idletasks()
    
def startDownloading():
    global file_size
    try:
        myList.delete(0,END)
        #configring Button
        searchButton.config(text="Search")
        searchButton.config(state=NORMAL)
        #featching the urlField
        url=urlField.get()
        if url=="":
            return
        #featching the resField
        res=resField.get()
        if ((res.isdigit())==False or res=="" or res not in itaglist):
            showinfo("Wrong Input!!","Please choose the valid Option")
            return
        downloadButton.config(text="Please wait...")
        downloadButton.config(state=DISABLED)
        path_to_save_video=askdirectory()
        if path_to_save_video is None:
            return
        
        ob=YouTube(url, on_progress_callback=progress)

        #progressbar
        global progressBar
        progressBar = Progressbar(main, orient = HORIZONTAL,length = 100, mode = 'determinate')
        progressBar.pack(pady = 10)
        
        #resolution selection
        strm=ob.streams.get_by_itag(int(res))
        
        #store the size of the file
        file_size=strm.filesize

        # show the Title
        vTitle.config(text=strm.title)
        vTitle.pack(side=TOP)

        #download video
        strm.download(path_to_save_video)

        #configring Button
        downloadButton.config(text="Download")
        downloadButton.config(state=NORMAL)

        # clear urlField , resField , taglist and processBar
        urlField.delete(0,END)
        resField.delete(0,END)
        progressBar.pack_forget()
        taglist=[]
        
        #remove title from main
        vTitle.pack_forget()
        showinfo("Download Fineshed","Downloaded Successfully")
        
    except Exception as e:
        print(e)
        print("error!!")


#searching for diffrent resolutions
def resolution():
    searchButton.config(text="Please wait...")
    searchButton.config(state=DISABLED)
    youtubeLink=urlField.get()
    youtubeObj=YouTube(youtubeLink)
    global file
    file=youtubeObj.streams

    #sb=Scrollbar()
    #sb.pack(side=RIGHT,fill=Y)
    myList.pack(side=BOTTOM,ipadx=100,pady=5)

    myList.insert(END,"id  res  size")

    
    for num in file:
        myList.insert(END,str(num.itag)+"  "+str(num.resolution)+"  "+str(num.filesize/1000000)+" MB")
        itaglist.append(str(num.itag))
        
    #sb.config(command=mylist.yview)
    
#creat new thread
def startSearchingThread():
    thread1=Thread(target=resolution)
    thread1.start()
def startDownloadThread():
    thread2=Thread(target=startDownloading)
    thread2.start()
    
    
if __name__=="__main__":
    # GUI
    main=Tk()
    main.geometry("600x7000")

    # Title
    main.title("YouTube Video Downloader")

    # Icon
    main.iconbitmap("you_tube.ico")

    file=PhotoImage(file="youtube.png")
    headingIcon=Label(main,image=file)
    headingIcon.pack(side=TOP)

    #listbox
    global myList
    myList=Listbox(main)
    
    #lable for url
    lab1=Label(main,text='Enter the URL of YouTube video:')
    lab1.pack(side=TOP)
    # url textfield
    urlField=Entry(main,font=("verdana",16),justify=CENTER)
    urlField.pack(side=TOP,fill=X,padx=10,pady=5)

    # search the url
    searchButton=Button(main,text="Search",font=("verdana",16),relief="ridge",command=startSearchingThread)
    searchButton.pack(side=TOP,pady=10)

    # Download Buttom
    downloadButton=Button(main,text="Download",font=("verdana",16),relief="ridge",command=startDownloadThread)
    downloadButton.pack(side=BOTTOM,pady=5)

    #Resolution textfield
    resField=Entry(main,font=("verdana",16),justify=CENTER)
    resField.pack(side=BOTTOM,fill=X,padx=200,pady=5)
    
    #lable for resolution
    lab2=Label(main,text='select the Resolution id:')
    lab2.pack(side=BOTTOM)

    
    #Video Title
    vTitle=Label(main,text="video Title")
                    
    main.mainloop()
