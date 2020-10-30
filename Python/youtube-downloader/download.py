from pytube import YouTube
# first we'll take the user input of link
link = input("Please enter you tube video link ")
yt = YouTube(link)

#Showing details of video
print("Title of the video is: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

# lists out best resolution
print(yt.streams.filter(progressive=True))

# Downloading video in best reslution
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading your video...")
ys.download()
print("Download of video completed!!")
