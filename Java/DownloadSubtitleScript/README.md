# Download subtitle script from [http://thesubdb.com/]
The aim of the program is to fetch the subtitles for a particular video file from the subDB repository via their API endpoint.

## Library Used:
*No external libraries used*

## API Documentation:
* The [SubDB](http://thesubdb.com/api/) API is used. 
* The API requires the hash value of the video file to match with their database subtitle file. Inorder to get the hash value their own function is being used to generate it in this program. 
* The API also requires a valid User-Agent to be sent along with the headers.
* The basic GET and POST operations are functional in this API.

## Usage: 
`>> javac DownloadSubtitleScript.java`

`>> java DownloadSubtitleScript`

## I/O:
```
Example:

Enter file name with extension: dexter_sample_video.mp4
(must be in the same path that of the java file)

Enter client name: Haripriya

Enter client version: 1.0

Enter client URL: https://github.com/HaripriyaB

Subtitles saved in dexter_sample_video.mp4.srt file
```
