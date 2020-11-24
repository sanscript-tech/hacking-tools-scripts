import numpy as np
from PIL import Image, ImageDraw

# Enter the diameter
diameter = input("Enter the diameter:")

# Open the input image as numpy array after resizing it, and then convert to RGB
img=Image.open("sunflower.jpg").convert("RGB")
modifiedSize = int(diameter);
img = img.resize((modifiedSize,modifiedSize));
npImage=np.array(img)
width, height = img.size 

# Create same size alpha layer with circle
alpha = Image.new('L', img.size,0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([0,0,height,width],0,360,fill=255)

# Convert alpha Image to numpy array
npAlpha=np.array(alpha)

# Add alpha layer to RGB
npImage=np.dstack((npImage,npAlpha))

# Save with alpha and then save it has circularImg.png
Image.fromarray(npImage).save('circularImg.png')
