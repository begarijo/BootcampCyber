# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/24 16:08:21 by begarijo          #+#    #+#              #
#    Updated: 2023/04/24 20:15:55 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse

from PIL import Image, ExifTags
from PIL.ExifTags import TAGS

def arguments():
    arg = argparse.ArgumentParser(description="Scorpion")
    arg.add_argument("IMG", help="Image to analyze")
    arg.add_argument("IMGS", help="Images to analyze", nargs="*")
    return arg.parse_args()

def meta_data(img):
    print("Filename ".ljust(29), ":", img.filename)
    print("Size ".ljust(29), ":", img.size)
    print("Height ".ljust(29), ":", img.height)
    print("Width ".ljust(29), ":", img.width)
    print("Format ".ljust(29), ":", img.format)
    print("Mode ".ljust(29), ":", img.mode)


def scorpion(path):
    for imgs in path:
        try:
            img = Image.open(imgs)
        except:
            print("Error")
        else:
            data = img.getexif()
            print(imgs.split("/")[-1])
            print("-"*60)
            meta_data(img)
            if not data:
                print("Image has no exif data")
            for key, val in data.items():
                if key in ExifTags.TAGS:
                    print(f'{ExifTags.TAGS[key]:30}: {val}')
        print('')


if (__name__=='__main__'):
    args = arguments()
    path = list()
    path.append(args.IMG)
    path += args.IMGS
    scorpion(path)

