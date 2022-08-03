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
        print("Image Encoded Sucessfully")


# LSB-STEGANOGRAPHY
def main():
    func = input("1: Encode\n2: Decode\n")
    src = input("Enter Source Image Path\n")

    if func == '1':
        message = input("Enter Message to Hide\n")
        dest = input("Enter Destination Image Path\n")
        print("Encoding...")
        encode(src, message, dest)

    if func == '2':
        print("Decoding...")


if __name__ == "__main__":
    main()
