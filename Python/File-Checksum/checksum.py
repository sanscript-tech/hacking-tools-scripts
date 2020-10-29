import sys
import hashlib
import os

# Check if user has entered commandline arguments correctly.
if len(sys.argv) < 3:
    print("Provide necessary commandline arguments.")
    sys.exit()

# Extract hashing algorithm and check if its supported or not.
hash_algo = sys.argv[1]
if hash_algo not in hashlib.algorithms_available:
    print(f"{hash_algo} algorithm is not supported.\n")
    print("Supported algorithms are as follows:")
    print(*hashlib.algorithms_available, sep="\n")
    sys.exit()

# Extract file path and check if its a file or not.
file_path = sys.argv[2]
if not os.path.isfile(file_path):
    print("Provided file does not exist.")

# Create a new hash object.
hash_ = hashlib.new(hash_algo)

# Open the file and read the data in chunks of 4096 bytes.
with open(file_path, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        hash_.update(chunk)

# Print the generated hash checksum.
print(f'{hash_algo} checksum for {os.path.split(file_path)[1]} is:\n{hash_.hexdigest()}')
