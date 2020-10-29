import sys
import hashlib
import os

if len(sys.argv) < 3:
    print("Provide necessary commandline arguments.")
    sys.exit()

hash_algo = sys.argv[1]
if hash_algo not in hashlib.algorithms_available:
    print(f"{hash_algo} algorithm is not supported.\n")
    print("Supported algorithms are as follows:")
    print(*hashlib.algorithms_available, sep="\n")
    sys.exit()

file_path = sys.argv[2]

hash_ = hashlib.new(hash_algo)

with open(file_path, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        hash_.update(chunk)

print(f'{hash_algo} checksum for {os.path.split(file_path)[1]} is:\n{hash_.hexdigest()}')
