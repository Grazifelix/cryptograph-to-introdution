# 02/08/22
# Graziela Felix
# Following the tutorial from Medium by Devang Jain

# import libraries
import numpy as np
from PIL import Image

# enconde fuction
def Encode(src, message, dest):
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(imag.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size//n

# LSB-STEGANOGRAPHY
def main():
    func = input("1: Encode\n2: Decode\n")
    src = input("Enter Source Image Path\n")

    if func == '1':
        message = input("Enter Message to Hide\n")
        dest = ("Enter Destination Image Path\n")
        print("Encoding...")

    if func == '2':
        print("Decoding...")

if __name__ == "__main__":
    main()

