import os
import hashlib
import sys

def get_hash(filename):
    read_size = 64 * 1024
    with open(filename, 'rb') as f:
        data = f.read(read_size)
        f.seek(-read_size, os.SEEK_END)
        data += f.read(read_size)
    return hashlib.md5(data).hexdigest()

if sys.argv[1] is not None:
    print(get_hash(sys.argv[1]))
else:
    print("-1")