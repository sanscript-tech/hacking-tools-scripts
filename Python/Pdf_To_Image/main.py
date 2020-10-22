import os
import sys
from pdf2image import convert_from_path

def convert_pdf_to_image(pdfpath,outputpath):
  images = convert_from_path(pdfpath)
  i = 1
  for image in images:
      image.save(outputpath+str(i) + '.jpg', 'JPEG')
      i = i + 1
  print("Pdf to image converted successfully")



if __name__ == "__main__":
  convert_pdf_to_image(sys.argv[1],sys.argv[2])
