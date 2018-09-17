import os
from PIL import Image, ImageDraw, ImageFont
import random
from PyLyrics import *
import warnings

warnings.filterwarnings("ignore")

# Take in user input until user says finished. Use PyLyrics to
# edit songList.txtself.

file = open("/home/anj/Documents/CSProjects/Changer/songList.txt", "a")

def checkFinished(text):
    return text == "finished"

def findSongs(self):
    print("Type 'finished' when you are done.")

    while True:
        artist = raw_input("Enter the artist: ")
        if checkFinished(artist):
            file.close()
            exit()
        song_title = raw_input("Enter the song title: ")
        if checkFinished(song_title):
            file.close()
            exit()

        error = False
        try:
           lyrics = PyLyrics.getLyrics(artist, song_title)
        except ValueError:
            print("The song could not be found. Double check the spelling")
            print("of both the song title and the artist's name.")
            error = True

        if error == False:
            file.write(song_title + " by " + artist)
            file.write("\n")
            file.write("\n")
            file.write(PyLyrics.getLyrics(artist, song_title))
            file.write("\n//$\n")
            findSongs(None)

findSongs(None)
