# Extract Image Metadata
The aim of the program is to generate the metatdata of an image given as input. Metadata is "data that provides information about other data". In other words, it is "data about data". 

## Libraries Used:
* Python [Pillow](https://pypi.org/project/Pillow/) - Python Imaging Library

## Prerequisites:
Install Pillow using the following command(pip/pip3):

`>> pip3 install Pillow`

## Usage:

Sample images given along with the source code

```
Enter path to the image file: $(imagename)

<If there exists Metadata of the input image, then it goes below>

Sample:

ExifVersion              : 0220
ComponentsConfiguration  : 
ShutterSpeedValue        : 5.643
DateTimeOriginal         : 2020:08:13 14:04:39
DateTimeDigitized        : 2020:08:13 14:04:39
ApertureValue            : 1.69
BrightnessValue          : 0.55
ExposureBiasValue        : 0.0
MaxApertureValue         : 1.69
MeteringMode             : 2
Flash                    : 0
FocalLength              : 5.23
ColorSpace               : 1
ExifImageWidth           : 2888
FocalLengthIn35mmFilm    : 24
SceneCaptureType         : 0
ExifImageHeight          : 1984
Model                    : SM-A715F
Orientation              : 1
Make                     : samsung
SensingMethod            : 1
XResolution              : 72.0
YResolution              : 72.0
ExposureProgram          : 2
GPSInfo                  : {29: '2020:08:13', 5: b'\x00', 6: 0.0}
ISOSpeedRatings          : 250
ResolutionUnit           : 2
ExposureMode             : 0
FlashPixVersion          : 0100
WhiteBalance             : 0
Software                 : A715FXXU2ATG1
DateTime                 : 2020:08:13 14:05:15
ExifOffset               : 202
SubsecTime               : 701285
SubsecTimeOriginal       : 701285
SubsecTimeDigitized      : 701285
ExposureTime             : 0.02
FNumber                  : 1.8

<If no metadata available, then it shows>

No Metadata available for this image!

```


