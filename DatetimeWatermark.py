from PIL import Image, ImageDraw, ImageFont
import glob
import os

picturePaths = glob.glob('./*.jpg') + glob.glob('./*.jpeg')
textMargin = 16

for picturePath in picturePaths:
    picture = Image.open(picturePath)
    w, h = picture.size

    datetime = picture.getexif()[306].replace(":", "/", 2)
    font = ImageFont.truetype("arial.ttf", max(w, h) // 16)

    draw = ImageDraw.Draw(picture)
    _, _, textW, textH = draw.textbbox((0, 0), datetime, font = font)
    draw.text((w - textW - textMargin, h - textH - textMargin), datetime, fill = "#FF0000", font = font, align = "right")

    splitPath = os.path.splitext(picturePath)
    newFileName = splitPath[0] + "_datetime" + splitPath[1]
    picture.save(newFileName, exif = picture.info['exif'])
