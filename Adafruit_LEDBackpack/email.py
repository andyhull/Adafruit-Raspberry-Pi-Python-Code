#!/usr/bin/env python
import os

import time

import datetime
from Adafruit_8x8 import ColorEightByEight

DEBUG = 1
os.system("export ENAME")
os.system("export EPASS")
USERNAME = os.environ["ENAME"]  # just the part before the @ sign, add yours here
PASSWORD = os.environ["EPASS"] 

NEWMAIL_OFFSET = 0        # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 30      # check mail every 60 seconds

# GPIO.setmode(GPIO.BCM)
# GREEN_LED = 18
# RED_LED = 23
# GPIO.setup(GREEN_LED, GPIO.OUT)
# GPIO.setup(RED_LED, GPIO.OUT)
# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
grid = ColorEightByEight(address=0x70)

print "Press CTRL+Z to exit"

smile_bmp = [0b00011110,0b00100001,0b11010010,0b11000000,0b11010010,0b11001100,0b00100001,0b00011110]
neutral_bmp = [0b00011110,0b00100001,0b11010010,0b11000000,0b11011110,0b11000000,0b00100001,0b00011110]
frown_bmp = [0b00011110,0b00100001,0b11010010,0b11000000,0b11001100,0b11010010,0b00100001,0b00011110]

grid.setBrightness(15)

while True:

        newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])

        if DEBUG:
                print "You have", newmails, "new emails!"

        if newmails > NEWMAIL_OFFSET:
                # Write a frown face
                for i in range(0,8):
                  grid.writeRowRaw(i, frown_bmp[i]) 
                time.sleep(1)
        else:
                # Write a smiley face
                for i in range(0,8):
                  grid.writeRowRaw(i, smile_bmp[i]) 
                time.sleep(1)

        time.sleep(MAIL_CHECK_FREQ)



