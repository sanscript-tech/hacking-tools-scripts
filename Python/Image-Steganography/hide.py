import cv2
import numpy as np
import sys
from cryptography.fernet import Fernet

# Check if the user has entered commandline arguments correctly or not.
if len(sys.argv) < 3:
    print("Provide appropriate commandline arguments.")
    sys.exit()


# Method to convert various data to binary.
def message_to_binary(message):
    if type(message) == str:
        return ''.join([ format(ord(i), "08b") for i in message ])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [ format(i, "08b") for i in message ]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")


# Method to generate key and encrypt secrect message.
def encrypt_message(message):
    key = Fernet.generate_key()
    encrypted_message = Fernet(key).encrypt(message.encode())

    return encrypted_message, key


# Method to embed encrypted message within the image.
def hide_info(image, message):

    # Encrypt the message.
    enc_message, key = encrypt_message(message)
    enc_message = enc_message.decode()

    # Get the maximum amount of byte data that can be embeded within the image.
    max_bytes = image.shape[0] * image.shape[1] * 3//8

    # Check if the data is within limits.
    if len(enc_message) > max_bytes:
        raise ValueError("Insufficient bytes, provide bigger image or shorter message.")

    # Add salt delimiter.
    enc_message += "#####"

    data_index = 0
    bin_enc_message = message_to_binary(enc_message)

    data_len = len(bin_enc_message)

    # Initiate embedding process.
    for values in image:
        for pixel in values:
            # Convert pixel data to binary.
            r, g, b = message_to_binary(pixel)

            # modify the least significant bit remaining data is available.
            if data_index < data_len:
                # Hide data into LSB of red pixel
                pixel[0] = int(r[:-1] + bin_enc_message[data_index], 2)
                data_index += 1

            if data_index < data_len:
                # Hide data into LSB of green pixel
                pixel[1] = int(g[:-1] + bin_enc_message[data_index], 2)
                data_index += 1

            if data_index < data_len:
                # Hide data into LSB of blue pixel
                pixel[2] = int(b[:-1] + bin_enc_message[data_index], 2)
                data_index += 1

            # Break out of the loop if there isn't any data left to embed.
            if data_index >= data_len:
                break

    # Save the encryption key in a file.
    with open("key", "wb") as f:
        f.write(key)

    return image


# Extract image and message path.
image_path = sys.argv[1]
message_path = sys.argv[2]


# Load image and message to memory.
source_image = cv2.imread(image_path)
with open(message_path, "r") as f:
    message = f.read()


# Perform the embeded operation and save the resultant image.
secret_image = hide_info(source_image, message)
secret_image_path = image_path.split(".")
secret_image_path = secret_image_path[-2]+"_secret."+secret_image_path[-1]
cv2.imwrite(secret_image_path, secret_image)
print("Message successfully hidden.")
