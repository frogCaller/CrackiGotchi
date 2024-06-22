# THIS PYTHON SCRIPT DOES NO CRACK ANY PASSWORDS !!
# IT ONLY DISPLAYS RANDOM PASSWORDS FROM ROCKYOU.TXT
# & DISPLAYS RANDOM CHARACTERS


import time
import datetime
from datetime import datetime
import sys
import os
import pygame
import logging
from PIL import Image, ImageDraw, ImageFont
from drive import SSD1305
import random
import subprocess

disp = SSD1305.SSD1305()

disp.Init()

# Clear display.
logging.info("clear display")
disp.clear()

# Create blank image for drawing.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
padding = 0
top = padding
bottom = height-padding
x = 0

timeframe = 0.01
# Load default font.
font = ImageFont.truetype('04B_08__.TTF',8)

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$&_-()=%*:/!?+."

def pick_random_line(file_name):
  """Choose a line at random from the text file"""
  with open(file_name, 'r') as file:
    lines = file.readlines()
    random_line = random.choice(lines)
    return random_line

def passwordguess(passlength):
    string = lower + upper + numbers + symbols
    password = "".join(random.sample(string, passlength))
    return password

def buffer(sec):
    disp.getbuffer(image)
    disp.ShowImage()
    time.sleep(sec)
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

def linetext(line, content):
    draw.text((x, top+line), content, font=font, fill=255)

display_count = 0

while True:
    try:
        current_date = datetime.now()
        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        #Date & Time
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        linetext(0, str(current_date.strftime("%A") + "         " + str(current_date.strftime("%-I:%M %p"))))
        linetext(16, str(current_date.strftime("%B %d %Y")))

        buffer(3)

        for m in range(500):
            linetext(0, "Rockyou.txt")
            linetext(16, "" + pick_random_line("rockyou.txt"))
            buffer(0.025)

        for m in range(500):
            linetext(0, "Brute Force")
            linetext(16, "" + passwordguess(15))
            buffer(0.025)

    except(KeyboardInterrupt):
        print("\n")
        break
