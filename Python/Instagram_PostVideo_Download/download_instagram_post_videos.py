# Import statements
import os
import requests
import urllib.request


def video_downloader(shortcode, videos_path):
    # fetch the instagram post from url appended with shortcode of the post
    videos = requests.get(f"https://www.instagram.com/p/{shortcode}/?__a=1")
    # fetch using JSON 
    video_url = videos.json()['graphql']['shortcode_media']['video_url']
    file_name = videos.json()['graphql']['shortcode_media']['taken_at_timestamp']
    download_path = f"{videos_path}/{file_name}.mp4"
    # Check if file already exists else download the videos
    if not os.path.exists(download_path):
        print(f"Downloading {file_name}.mp4...........")
        # Retrieveing data from url
        urllib.request.urlretrieve(video_url, download_path)
        print(f"{file_name}.mp4 downloaded.")
    else:
        print(f"{file_name}.mp4 has been downloaded already.")

# get the current working directory to save the downloaded video
path = os.getcwd();
# get shortcode from user for the post
post_id = input("Enter shortcode of the post: ")

# video downloading starts
video_downloader(post_id,path)