from zipfile import ZipFile

def main():
    # Enter the name of zip file
    zipFile = input("Enter zip file:")
    # Enter the path of the file to be extracted
    extractFile = input("Enter path of the file:")
    print("Extracted file in ZIP to current directory")
    # create a ZipFile object in READ mode and name it as zipObj
    with ZipFile(zipFile, 'r') as zipObj:
       # extract() method is used to extract any file by specifying its path in the zip file
       zipObj.extract(extractFile);

if __name__ == '__main__':
   main()
