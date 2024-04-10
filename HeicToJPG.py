from PIL import Image
from pillow_heif import register_heif_opener
import glob
import os

register_heif_opener()
picturePaths = glob.glob('./*.heic')

for picturePath in picturePaths:
    picture = Image.open(picturePath).convert('RGB')
    newFileName = os.path.splitext(picturePath)[0] + ".jpg"
    picture.save(newFileName, exif = picture.info['exif'])
