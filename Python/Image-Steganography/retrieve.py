from cryptography.fernet import Fernet
import cv2
import numpy as np
import sys


# Check if user has provided commandline arguments or not.
if len(sys.argv) < 3:
    print("Provide appropriate commandline arguments.")
    sys.exit()


# Convert various data to binary.
def message_to_binary(message):
    if type(message) == str:
        return ''.join([ format(ord(i), "08b") for i in message ])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [ format(i, "08b") for i in message ]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")


# Decrypt an encrypted message.
def decrypt_message(enc_message, key):
    dec_message = Fernet(key).decrypt(enc_message)
    return dec_message


# Retrive the message from an image.
def retrieve_info(image, key):

    binary_data = ""

    for values in image:
        for pixel in values:
            # Convert pixel to binary.
            r, g, b = message_to_binary(pixel)

            # Extracting data from the LSB of all the channels.
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]

    # split by 8 bits.
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]

    # Convert to ASCII values.
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####":
            break

    # Decrypt the encryption.
    message = decrypt_message(decoded_data[:-5].encode(), key).decode()

    return message


# Extract the image and key path.
image_path = sys.argv[1]
key_path = sys.argv[2]


# Read the image and key.
steg_image = cv2.imread(image_path)
with open(key_path, "rb") as f:
    key = f.read()

# Display the secrect message.
print(f"Secret Message:{retrieve_info(steg_image, key)}")
