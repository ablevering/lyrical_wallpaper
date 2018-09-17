import os
from PIL import Image, ImageDraw, ImageFont
import random
from PyLyrics import *

# Take in user input until user says finished. Use PyLyrics to
# edit songList.txtself.
file = open("/home/anj/Documents/CSProjects/Changer/songList.txt", "a")

def checkFinished(text):
    return text == "finished"

# Put the contents of songList.txt onto the background and save
def writeFile():

    file = open("/home/anj/Documents/CSProjects/Changer/songList.txt", "r")
    contents = file.read()
    songList = contents.split("//$")
    song = random.choice(songList)

    while song.strip() == "":
        song = random.choice(songList)

    file.close()

    im = Image.open("/home/anj/Documents/CSProjects/Changer/cleanBackground.jpg")
    draw = ImageDraw.Draw(im)

    lines = song.split("\n")
    x = 110
    y = 150
    longestLine = 0

    for line in lines:
        draw.text((x, y), line, (0, 0, 0), ImageFont.truetype("/usr/share/fonts/truetype/freefont/Kinnari.ttf", 14, encoding="unic"), anchor=None)
        y += 17
        if len(line) > longestLine:
            longestLine = len(line)
        if y > 550:
            x += longestLine * 7
            y = 201
    im.save("/home/anj/Documents/CSProjects/Changer/background.jpg")
    im.close()

    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/anj/Documents/CSProjects/Changer/background.jpg")

writeFile()
