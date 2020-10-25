import cv2
capture = cv2.VideoCapture(0)
while capture.isOpened():
    # reading the capture image
    state,image = capture.read()
    # proceed if capture is successful
    if state:
        cv2.imshow("background",image)
        #stop when z key is pressed
        if cv2.waitKey(4) == ord('z'):
            cv2.imwrite('background-image.jpg',image)
            break
    else:
        print("Background image was not captured")
capture.release()
cv2.destroyAllWindows()
