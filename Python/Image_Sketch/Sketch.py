# Importing Libraries
import cv2
import numpy as np
from skimage import io
from PIL import Image

# Making a sketch generating function

def sketch(img):
    # Converting image into grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    RGB_img = cv2.cvtColor(img_gray, cv2.COLOR_BGR2RGB)

    # Clean up image using Gausian Blur
    img_gray_blur = cv2.GaussianBlur(RGB_img, (5, 5), 0)

    # Extracting edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)

    # Do an invert binarize the image
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

# Reading our image

filename = input("Enter the file name: ")
img = Image.open(filename)
#img = io.imread("obama.jpg")
cv2.imshow('Our Sketch', sketch(img))
# cv2.imwrite('sketch.jpg', sketch(img))
cv2.waitKey(0)
cv2.destroyAllWindows()

