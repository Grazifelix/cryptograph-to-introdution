# 02/08/22
# Graziela Felix
# Following the tutorial from Medium by Devang Jain

# import libraries
import numpy as np
from PIL import Image


# enconde fuction
def encode(src, message, dest):
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    n = 0
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size//n

    message += '$t3g0'
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("ERROR: need a larger file size")
    else:
        index = 0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1
        array = array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(f"{dest}/enc_img.png")
        print("\u001b[37m \u001b[45m Image Encoded Sucessfully \u001b[m")


# decode function
def decode(src):
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size // n

    #  extract the least significant bits from each of the pixels
    #  and convert these groups into ASCII characters to find the hidden message
    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])
    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))

    #check if the delimiter was found or not.
    # If not, that means there was no hidden message in the image.
    if "$t3g0" in message:
        print("\u001b[37m \u001b[45m Hidden Message:\u001b[m", message[:-5])
    else:
        print("\u001b[37m \u001b[45m No hidden Message Found \u001b[m")


# LSB-STEGANOGRAPHY
def main():
    func = input("\u001b[35m1: Encode\n2: Decode\n \u001b[m")
    src = input("\u001b[35m Enter Source Image Path\n \u001b[m")

    if func == '1':
        message = input("\u001b[35m Enter Message to Hide\n \u001b[m")
        dest = input("\u001b[35m Enter Destination Image Path\n \u001b[m")
        print("\u001b[35m Encoding...\u001b[m")
        encode(src, message, dest)

    if func == '2':
        print("\u001b[3m \u001b[35m Decoding...\u001b[m")
        decode(src)

if __name__ == "__main__":
    main()
