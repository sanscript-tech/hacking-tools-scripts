#!/usr/bin/env python3

import hashlib
import os
import requests
import glob
# FILE_TYPES = ["*.mp4", "*.avi", "*.mkv"]
 # getting the hash of the file
def get_hash(filename):
    read_size = 64 * 1024
    with open(filename, 'rb') as f:
        data = f.read(read_size)
        f.seek(-read_size, os.SEEK_END)
        data += f.read(read_size)
    return hashlib.md5(data).hexdigest()

filename = input('Please enter the name of the file in current directory whose subtitiles you wish to extract ')
print("Getting subtitles for your file : {} ".format(filename))
# making get request to the API
try:
    headers = {'User-Agent': 'SubDB/1.0 (paradoxical-sub/1.0; https://github.com/TaniaMalhotra/hacking-tools-scripts)'}
    url = "http://api.thesubdb.com/?action=download&hash=" + get_hash(filename) + "&language=en"
    response = requests.get(url, headers=headers)
    #saving subtitles in a file
    with open("output" + ".srt", "w") as sub:
        sub.write(response.text)
    print("Subtitles saved in output.srt file")

# if subtitles not found
except:
    print("Sorry your file does not seem to be present in subdub database.")
