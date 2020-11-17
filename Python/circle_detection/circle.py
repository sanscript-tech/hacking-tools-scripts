#importing libraries required
import numpy as np
import cv2 as cv
#reading image
img = cv.imread('img.jpeg')
output = img.copy()
#converting image to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
#hough circle detection method for circle detection
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20,
                          param1=50, param2=30, minRadius=0, maxRadius=0)
#all detected circles 
detected_circles = np.uint16(np.around(circles))
# looping on all detected circles to print centroid coordinates and radius
for (x, y ,r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (0, 0, 0), 3)
    cv.circle(output, (x, y), 2, (0, 255, 255), 3)
    print("center x={},y={},radius = {}\n".format(x,y,r))

#showing the output image
cv.imshow('output',output)
cv.waitKey(0)
cv.destroyAllWindows()
