# importing sys , pdf2image wrapper library
import os
import sys
from pdf2image import convert_from_path

# function to convert pdf to image , takes pdfpath and outputpath as parameters given in command line arguments

def convert_pdf_to_image(pdfpath,outputpath):
  images = convert_from_path(pdfpath)   # convert_from_path() is a predefined function for conversion
  i = 1
  for image in images:
      image.save(outputpath+str(i) + '.jpg', 'JPEG')  # saving the images as  - eg : 1.jpg
      i = i + 1
  print("Pdf to image converted successfully") # success mesaage 


# main function

if __name__ == "__main__":
  convert_pdf_to_image(sys.argv[1],sys.argv[2]) # calling convert_pdf_image() with pdfpath and outputpath parameters
