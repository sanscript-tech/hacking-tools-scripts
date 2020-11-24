from PIL import Image
from PIL.ExifTags import TAGS

# path to the image or video
imagename = input("Enter path to the image file: ")

# read the image data using PIL
try:
    image = Image.open(imagename)
except:
    print("Image not readable!")
    exit()

# extract EXIF data
exifdata = image.getexif()

# If no metadata is available for the image
if len(exifdata) == 0:
    print("No Metadata available for this image!")

# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")
