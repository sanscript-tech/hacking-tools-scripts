# Image resizing tool<a name="TOP"></a>
- - - - - - 
# About the script

The aim of the script is to resize the image lying in a directory to the desired dimensions as are input by the user. This has been achieved using Image class from PIL module.

# Requirements

```pip install pillow```

# How to run

Place the script in the directory containing the images and run ```python image-resizer.py```

 If it is desirable to resize ```original-image1.jpg``` then follow the directory structure below for placement of script
.  
    
    ├── README.md
    ├── original-image1.jpg
    ├── image resizer.py #script goes here
    ├── images          #  Images folder
    │   ├── original-image2jpg
    │   ├── image2.jpg    
    │   ├── image3.jpg        
    └── ...

 If it is desirable to resize ```original-image2jpg``` lying inside the images folder, then place the script in the same folder. Below is an example directory structure.


    ├── README.md
    ├── original-image1.jpg
    ├── images          #  Images folder
    │   ├── original-image2jpg
    |   ├── image resizer.py #script goes here
    │   ├── image2.jpg    
    │   ├── image3.jpg        
    └── ...
    
## Alternatively
You may place the script anywhere in the directory and specify the path of the image inside the current directory when prompted to do the same. </br>
For instance you might enter ```images\\original-image2.jpg``` for accessing an image in images folder inside directory

# Example output

The following are resized images for different specified sizes

## 100x100px



![alt text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/image-resizer/Python/image-resizer/resized-image-examples/100x100.png)



## 500x500px



![alt text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/image-resizer/Python/image-resizer/resized-image-examples/500x500.png)


## 1000x1000px



![alt text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/image-resizer/Python/image-resizer/resized-image-examples/1000x1000.png)

