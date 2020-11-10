import subprocess

# check if spotdl is installed or not.
try:
    import spotdl
except ModuleNotFoundError:
    print("Kindly install spotdl using pip.")

# Method to download new song, album or playlist.
def download_new():
    track_url = input("Enter Spotify song/album/playlist URL:")
    subprocess.call(["spotdl", track_url])


# method to download multiple songs.
def download_multi():
    track_urls = input("Enter URLs of songs space separated:").split()
    subprocess.call(["spotdl", *track_urls])

# Method to resume a partially downloaded file.
def resume_download():
    partial_file = input("Enter path for tracking file[.spotDlTrackingFiles]:")
    subprocess.call(["spotdl", partial_file])

# Main method.
if __name__ == "__main__":
    choice = int(input(
    """[1] Initiate a new download(song, album, playlist).
[2] Download multiple songs.
[3] Resume incomplete download.
Enter your choice:"""))

    # Switch case to select the appropriate method.
    {
        1 : download_new,
        2 : download_multi,
        3 : resume_download
    }[choice]()
