import pyautogui
import cv2
import numpy as np
# the resolution of screen recording would be (1920,1080)
# Stating the codec of the video i.e. the format in which it wil be stored
codec = cv2.VideoWriter_fourcc(*"XVID")
# Name of the final recorded file

output_file = "Output.avi"

# This is an object which contains all specifications of our video file
video_writer_obj = cv2.VideoWriter(output_file, codec, 60.0, (1920, 1080))

# Making a new empty window and resizing it later
cv2.namedWindow("New_window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("New_video", 480, 270)

while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    video_writer_obj.write(frame)
    cv2.imshow('New_window', frame)

    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Releasing the output object
video_writer_obj.release()

# Destroy all windows
cv2.destroyAllWindows()
