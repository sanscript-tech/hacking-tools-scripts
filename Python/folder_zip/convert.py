from shutil import make_archive
import argparse
from os import path
from sys import exit

#argparse setup
parser = argparse.ArgumentParser()
parser.add_argument("directory",help="path of the directory/file that needs to be zipped")
parser.add_argument("zip_location",help="path of the zip file you need to store")
args = parser.parse_args()

#declaring global variables for directory and zip_location
zip_name = args.zip_location 
directory_name= args.directory


def path_checker(_path):
    '''
    checking if the paths exists
    returns True or False
    '''
    return path.exists(_path)

def make_zip():
    global zip_name,directory_name
    try:
        make_archive(zip_name,'zip',directory_name)
        print(f"zip file generated path: {zip_name}")
        return;
    except:
        print(f"Error!")
        return;

if __name__ == "__main__":
    if path_checker(directory_name):
        make_zip()
    else:
        print("invalid path")
    exit()
