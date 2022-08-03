# 02/08/22
# Graziela Felix
# Following the tutorial from Medium by Devang Jain

# import libraries
import numpy as np
from PIL import Image


# enconde fuction
def encode(src, message, dest):
    # convert the source image into a NumPy array of pixels
    # store the size of the image

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    # check if the mode of the image is RGB or RGBA and set the value of n
    n = 0
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    # calculate the total number of pixels.
    total_pixels = array.size//n

    # add a delimiter (“$t3g0") at the end of the secret message
    message += '$t3g0'
    # convert this updated message to binary form and calculate the required pixels.
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    # check if the total pixels available is sufficient for the secret message or not
    if req_pixels > total_pixels:
        print(f"{style_color_white}{style_bcg_magenta}ERROR: need a larger file size{style_clean}")
    else:
        # iterating the pixels one by one and modifying their least significant
        # bits to the bits of the secret message until the complete message including the delimiter has been hidden.
        index = 0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        # "have the updated pixels array and we can use this to create and save it as the destination output image"
        array = array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(f"{dest}/enc_img.png")
        print(f"{style_color_white}{style_bcg_magenta}Image Encoded Sucessfully{style_clean}")


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

    # check if the delimiter was found or not.
    # If not, that means there was no hidden message in the image.
    if "$t3g0" in message:
        print(f"{style_color_white}{style_bcg_magenta}Hidden Message:{style_clean}", message[:-5])
    else:
        print(f"{style_color_white}{style_bcg_magenta}No hidden Message Found{style_clean}")


# LSB-STEGANOGRAPHY
def main():

    func = input(f"{style_color_magenta}1: Encode\n2: Decode\n{style_clean}")
    src = input(f"{style_color_magenta}Enter Source Image Path\n{style_clean}")

    if func == '1':
        message = input(f"{style_color_magenta}Enter Message to Hide\n{style_clean}")
        dest = input(f"{style_color_magenta}Enter Destination Image Path\n{style_clean}")
        print(f"{style_color_magenta}{style_italic}Encoding...{style_clean}")
        encode(src, message, dest)

    if func == '2':
        print(f"{style_color_magenta}{style_italic}Decoding...{style_clean}")
        decode(src)


# styles
style_clean = '\u001b[m'
style_color_magenta = "\u001b[35m"
style_color_white = "\u001b[37m"
style_bcg_magenta = "\u001b[45m"
style_italic = "\u001b[3m"

if __name__ == "__main__":
    main()



