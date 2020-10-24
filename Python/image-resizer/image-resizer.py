import PIL
import os

# Importing Image class from PIL module
from PIL import Image

# Opens the image in RGB mode
CURRENT_DIR = os.getcwd()
name = input("Please enter the name of the image in the current directory that you would like to resize-->")
PATH = CURRENT_DIR + "\\" + name
img = Image.open(PATH)

#gets the current width and height of the image
cur_width, cur_height = img.size

#takes desired width and height input from the user
new_width = int(input("Please enter the required new width"))
new_height = int(input("Please enter the required new height"))

#calculating the resizing scale
scale = min(new_height/cur_height, new_width/cur_width)

#resizing image
img = img.resize(
    (int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)

# Shows the resized image in image viewer
img.show()
