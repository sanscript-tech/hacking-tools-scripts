from PIL import Image
import numpy as np
import sys
from cryptography.fernet import Fernet


if len(sys.argv) < 3:
    print("Provide appropriate commandline arguments.")
    sys.exit()


def encrypt_message(message):
    key = Fernet.generate_key()
    encrypted_message = Fernet(key).encrypt(message.encode())

    return encrypted_message, key


def hide_info(image, message):

    enc_message, key = encrypt_message(message)
    image = np.array(image)

    max_bytes = image.shape[0] * image.shape[1] * 3//8

    if len(enc_message) > max_bytes:
        raise ValueError("Insufficient bytes, provide bigger image or shorter message.")

    enc_message += "#####".encode()

    data_index = 0
    bin_enc_message = [ format(i, "08b") for i in enc_message]

    data_len = len(bin_enc_message)

    for values in image:
        for pixel in values:
            r, g, b = [format(i, "08b") for i in pixel]

            if data_index < data_len:
                pixel[0] = int(r[:-1] + bin_enc_message[data_index], 2)
                data_index += 1

            if data_index < data_len:
                pixel[1] = int(g[:-1] + bin_enc_message[data_index], 2)
                data_index += 1

            if data_index < data_len:
                pixel[2] = int(b[:-1] + bin_enc_message[data_index], 2)
                data_index += 1

            if data_index >= data_len:
                break

    with open("key", "wb") as f:
        f.write(key)

    return Image.fromarray(image)


image_path = sys.argv[1]
message_path = sys.argv[2]

source_image = Image.open(image_path, "r")
with open(message_path, "r") as f:
    message = f.read()

secret_image = hide_info(source_image, message)
secret_image_path = image_path.split(".")
secret_image_path = secret_image_path[-2]+"_secret."+secret_image_path[-1]
secret_image.save(secret_image_path)