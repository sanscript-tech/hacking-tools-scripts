import sys 
import hashlib

methods = {
  '1':'md5',
  '2':'sha1',
  '3':'sha256',
  '4':'sha512',
}

def help():
  print("Usage: python app.py filename")
  print("""
  Available hash methods
  [1] MD5
  [2] SHA1
  [3] SHA256
  [4] SHA512
  """)


def file_read(filename):
  try:      
    content = open(filename, "r").read()
    content = content.encode('utf-8')
    return content
  except:
    print("Openning file error")
    exit(0)

def hash_text(content,method):
  return hashlib.new(methods[method],content).hexdigest()


def write_content(hashed_content):
  new_file=open('Hased data.txt','w')
  new_file.write(hashed_content)
  new_file.close()
  print("Done writing data to file hash data.txt")

if __name__ == "__main__":
    help()
    if len(sys.argv) < 2:
      help()
      print("No file specified")
      exit(0)
    
    filename = sys.argv[1]

    content = file_read(filename)
    method=int(input())
    if(method > 4 or method < 1):
        print("No method or wrong method specified. Using default md5 hashing method")
        method = 1

    hashed_content = hash_text(content,str(method))

    write_content(hashed_content)