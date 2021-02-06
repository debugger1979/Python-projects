import os
import fileinput
from exif import Image
import fnmatch

img_path = "D:/Distr/foto"

for root, dirs, files in os.walk(img_path):
    print(root)