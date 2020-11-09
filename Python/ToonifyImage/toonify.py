import requests
import shutil # to save image locally
imagePath=input("Please enter the path of image to toonify : ")
r = requests.post(
    "https://api.deepai.org/api/toonify",
    files={
        'image': open(imagePath, 'rb'),
    },
    headers={'api-key': 'e6c65153-10a5-45f8-a24e-9d8d7ef4f76f'}
)
y=r.json()
image_url=y['output_url']
filename = image_url.split("/")[-1]
# Open the url image
r1 = requests.get(image_url, stream = True)
# Check if the image was retrieved successfully
if r1.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r1.raw.decode_content = True
    # Open a local file with wb ( write binary ) permission.
    with open(filename,'wb') as f:
        shutil.copyfileobj(r1.raw, f)
    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')
