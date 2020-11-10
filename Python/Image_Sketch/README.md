# Image to Sketch

### Introduction
This script converts original image into black and white sketched image.

## Third Party Libraries Required :
1. opencv library 
2. scikit-image library

### How to install above Library
Install the following libraries through command line:
```
pip install opencv-python
pip install numpy
pip install scikit-image
```
### How to use it :
1. Download or clone the repository
2. Install required libraries
3. Add path of your image in ```img = io.imread("enter your image path") ``` function from **Sketch.py**
4. Run **Sketch.py**
5. Your black and white sketched image will get displayed
6. If you want to save the image in the same directory then uncomment ```cv2.imwrite('sketch.jpg', sketch(img))``` and run **Sketch.py** again

### Results:

#### Original Image
<img src ="https://github.com/sharur7/Rotten-Scripts/blob/sharur7/Python/Image_Sketch/obama.jpg?raw=true" alt="Original_image" width="280" height="300">

#### Sketched Image
<img src ="https://github.com/sharur7/Rotten-Scripts/blob/sharur7/Python/Image_Sketch/sketch.jpg?raw=true" alt="Original_image" width="280" height="300">
