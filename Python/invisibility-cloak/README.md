# Invisibility cloak

- - - - - - - - - - - - -
![alt text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/invisibility-cloak/Python/invisibility-cloak/images/cloak-gif.gif)

## About the script
This script aims to create our own ‘Invisibility Cloak’ using simple computer vision techniques in OpenCV. This script has been written in  in Python because it provides
exhaustive and sufficient libraries to build this program. Here, we have created this magical experience using an image processing technique called ```Color detection and segmentation```.

## Requirements

```pip install opencv-python```</br>
```pip install numpy```</br>

## To run
In order to run this script, you must have a cloth of **same color and no other color should be visible into that cloth**. We are taking the red cloth. </br>
If you are taking some other cloth, the code will remain the same but with minute changes. You might need to tweak the colour values while using cloth of another colour.</br>

- First you will need to capture the background image of your surrounding:</br>
```python background-image.py```</br>
Press 'z' key to capture.</br>

- Next run ```invisible.py```</br>
Red pixels in the image will become invisible and be replaced by background image pixels.</br>

## Tweaking params a/t your cloth colour
If you aren't getting accurate results, it is because your shade/colour of cloth might be different as compared to whatis used in the script. So, you might need to change some parameters.</br>
```hsv_red = cv2.cvtColor(np.uint8([[[0,0,255]]]), cv2.COLOR_BGR2HSV)```</br>
Here ```[0,0,255]``` basically refers to the bgr colour of generic red clour. </br>
So if you're using another colour, you will have to change the values according to cloak shade.</br>

## Example output using this script
<img src="https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/invisibility-cloak/Python/images/invisibility-cloak/output.png" alt="alt text" width="400" height="300">
