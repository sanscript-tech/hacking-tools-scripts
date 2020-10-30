from cryptography.fernet import Fernet
from PIL import Image
import numpy as np
import sys

if len(sys.argv) < 3:
    print("Provide appropriate commandline arguments.")
    sys.exit()


image_path = sys.argv[1]
key_path = sys.argv[2]


def decrypt_message(enc_message, key):
    dec_message = Fernet(key).decrypt(enc_message)
    return dec_message


def retrieve_info(image, key):

    binary_data = ""
    image = np.array(image)

    for values in image:
        for pixel in values:
            r, g, b = [format(i, "08b") for i in pixel]
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]

    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]

    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####".encode():
            break

    message = decrypt_message(decoded_data[:-5].encode(), key)

    return decoded_data[:-5]


steg_image = Image.open(image_path, 'r')
with open(key_path, "rb") as f:
    key = f.read()

print(f"Secret Message:{retrieve_info(steg_image, key)}")
