#Imports and dependencies
#These packages are used for OCR(Optical character recognition)
import pytesseract
from PIL import Image
import sys

'''The script can be run by passing the path of the image as a Command Line argument as,

    python3 image-to-text.py "/path_of_image"

'''

def convert_image_to_text(image_path):
    text = ""
    #image_path = input("Enter the path of the image: ")
    text = pytesseract.image_to_string(Image.open(image_path))
    with open("Text_in_the_image.txt", "w") as file:
        file.write(text)
    return("Text in the image is successfully written to a text file in the same directory")

if __name__ == "__main__":
    print(convert_image_to_text(sys.argv[1]))
