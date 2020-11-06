import numpy as np
import cv2
from ffpyplayer.player import MediaPlayer
0
# PATH of the video
print('Enter the Path of the video')
path=input()

# text
print('Enter the Text')
text=input()

# org
print('Enter the coordinates of text')
location = tuple(map(int,input().split()))

# Blue color in BGR
print('Enter the color(Ex- 155 168 158)')
color = tuple(map(int,input().split()))

# cv2-fonts
Hershey_Simplex = cv2.FONT_HERSHEY_SIMPLEX
Hershey_Plain = cv2.FONT_HERSHEY_PLAIN
Hershey_Duplex = cv2.FONT_HERSHEY_DUPLEX
Hershey_Complex = cv2.FONT_HERSHEY_COMPLEX
Hershey_Triplex = cv2.FONT_HERSHEY_TRIPLEX
Hershey_Complex_Small = cv2.FONT_HERSHEY_COMPLEX_SMALL
Hershey_Script_Simplex = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
Hershey_Script_Complex = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
font_list_index=[['0','Hershey_Simplex'],['1','Hershey_Plain'],['2','Hershey_Duplex'],['3','Hershey_Complex'],['4','Hershey_Triplex'],['5','Hershey_Complex_Small'],['6','Hershey_Script_Simplex'],['7','Hershey_Script_Complex']]
font_list=[Hershey_Simplex,Hershey_Plain,Hershey_Duplex,Hershey_Complex,Hershey_Triplex,Hershey_Complex_Small,Hershey_Script_Simplex,Hershey_Script_Complex]

print('choose the font')
print('Id',' ','item')
for item in font_list_index:
    print(item[0],' ',str(item[1]))

Id = int(input())
font = font_list[Id-1]

# fontScale
fontScale = 1

# Window name in which image is displayed 
window_name = 'video'

# Line thickness of 2 px 
thickness = 2

video = cv2.VideoCapture(path)
player = MediaPlayer(path)

while(True):
    ret, frame = video.read()
    audio_frame, val = player.get_frame()
    if ret==True:
        # Using cv2.putText() method 
        image = cv2.putText(frame, text, location, font, fontScale, color, thickness, cv2.LINE_AA) 
           
        # Displaying the image 
        cv2.imshow(window_name, image)

        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame

    if cv2.waitKey(28) & 0xFF == ord('q'):
        break


# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
