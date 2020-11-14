from zipfile import ZipFile

def main():
    # Enter the name of zip file
    zipFile = input("Enter zip file:")
    # Enter the path of the file to be extracted
    print("Extracted file in ZIP to current directory")
    # create a ZipFile object in READ mode and name it as zipObj
    with ZipFile(zipFile, 'r') as zipObj:
       # extractall the files from a zip file
       zipObj.extractall();

if __name__ == '__main__':
   main()
