import os
import fileinput
from exif import Image
import fnmatch

img_path = "D:\\Distr\\foto"

for roots, dirs, files in os.walk(img_path):
    for file in files:
        full_name = os.path.join(roots, file)
        with open(full_name, 'rb') as image_file:
            my_image = Image(image_file)
            if my_image.has_exif:
                
        print()
