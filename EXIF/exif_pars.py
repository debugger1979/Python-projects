import os
import fileinput
from exif import Image
import fnmatch

img_path = "D:\\Distr\\foto"

for roots, dirs, files in os.walk(img_path):
    for file in files:
        
        print(os.path.join(roots, file))
