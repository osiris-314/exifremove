#!/usr/bin/env python3
import argparse
import os
from PIL import Image
from colorama import Fore

def remove_exif_data(input_image_path):
    try:
        with Image.open(input_image_path) as img:
            base, ext = os.path.splitext(input_image_path)
            output_image_path = f"{base}_no_exif{ext}"
            img.save(output_image_path, exif=b'')
            print(Fore.LIGHTBLUE_EX + 'Successfully Removed Exif Data From: ' + Fore.YELLOW + str(input_image_path) + Fore.RESET)
            print(Fore.CYAN + 'Output saved to: ' + Fore.LIGHTGREEN_EX + str(output_image_path) + Fore.RESET)
    except:
        print(Fore.RED + 'Failed To Remove The Data' + Fore.RESET)

def main():
    parser = argparse.ArgumentParser(description="Remove EXIF data from an image.")
    parser.add_argument('input', type=str, help="Path to the input image file")
    args = parser.parse_args()
    remove_exif_data(args.input)

if __name__ == "__main__":
    main()
