from zipfile import ZipFile

def main():
    # Enter the path of the zip file
    zipFile = input("Enter zip file:")
    print("Extracted file in ZIP to current directory")
    # create a ZipFile object in READ mode and name it as zipObj
    with ZipFile(zipFile, 'r') as zipObj:
       # extractall the files from a zip file
       zipObj.extractall();

if __name__ == '__main__':
   main()
