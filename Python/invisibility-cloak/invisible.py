import cv2
import numpy as np
capture = cv2.VideoCapture(0)
background = cv2.imread('./background-image.jpg')
while capture.isOpened():
    #going to read every frame
    state, image_frame = capture.read()
    if state:
        hsv = cv2.cvtColor(image_frame, cv2.COLOR_BGR2HSV)

        #putting in bgr colour value of red to convert to hsv
        # you might need to change the colour values depending on the type of cloth colour you have
        hsv_red = cv2.cvtColor(np.uint8([[[0,0,255]]]), cv2.COLOR_BGR2HSV)


        # lower range of red in hsvm: np.array([0, 100, 100])
        # upper range of red in hsv : np.array([10, 255, 255])

        mask = cv2.inRange(hsv,np.array([0, 100, 100]), np.array([10, 255, 255]))


        #mask for red objects
        mask1 = cv2.bitwise_and(background, background, mask=mask)
        mask = cv2.bitwise_not(mask)

        # mask for non-red objects
        mask2 = cv2.bitwise_and(image_frame, image_frame, mask=mask)
        cv2.imshow("magic-cloak", mask1 + mask2)
        if cv2.waitKey(4) == ord('z'):
            break

capture.release()
cv2.destroyAllWindows()
