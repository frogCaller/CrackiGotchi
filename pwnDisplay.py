import time
import random
import sys
sys.path.append('/home/pi/python/screen/drive')
import os
import requests
from datetime import datetime

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'drive')
if os.path.exists(libdir):
    sys.path.append(libdir)
import spidev
import logging
from drive import SSD1305

from PIL import Image,ImageDraw,ImageFont

import subprocess

# 128x32 display with hardware SPI:
disp = SSD1305.SSD1305()

disp.Init()

# Clear display.
logging.info("clear display")
disp.clear()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 0
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

timeframe = 0.01
# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
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
        linetext(8, str(current_date.strftime("%A") + "         " + str(current_date.strftime("%-I:%M %p"))))
        linetext(24, str(current_date.strftime("%B %d %Y")))

        buffer(3)

        for m in range(500): 
            linetext(0, "Rockyou.txt")
            linetext(16, "" + pick_random_line("/home/pi/python/rockyou.txt"))
            buffer(0.025)

        for m in range(500):  
            linetext(0, "Brute")
            linetext(16, "" + passwordguess(12))
            buffer(0.025)


    except(KeyboardInterrupt):
        print("\n")
        break
