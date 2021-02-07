import os
import fileinput
import fnmatch
from PIL import Image
from PIL.ExifTags import TAGS

#img_path = "D:\\Distr\\foto"
img_path = "F:\\foto"

def get_exif(filename):
    i = Image.open(filename)
    info = i._getexif(a)
    return {TAGS.get(tag): value for tag, value in info.items()}

for roots, dirs, files in os.walk(img_path):
    for file in files:
        full_name = os.path.join(roots, file)
        if fnmatch.fnmatch(full_name, '*.jpg'):
            print(get_exif(full_name))
 #       with open(full_name, 'rb') as image_file:
 #           my_image = Image(image_file)
 #           if my_image.has_exif:
 #               print(full_name)
 #               print()

                
