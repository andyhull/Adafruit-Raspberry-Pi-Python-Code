#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import ColorEightByEight

# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
grid = ColorEightByEight(address=0x70)

print "Press CTRL+Z to exit"

smile_bmp = [0b00011110,0b00100001,0b11010010,0b11000000,0b11010010,0b11001100,0b00100001,0b00011110]
neutral_bmp = [0b00011110,0b00100001,0b11010010,0b11000000,0b11011110,0b11000000,0b00100001,0b00011110]
frown_bmp = [0b00011110,0b00100001,0b11010010,0b11000000,0b11001100,0b11010010,0b00100001,0b00011110]

grid.setBrightness(15)

for x in range(1, 4):
  for y in range(1, 4):
    grid.setPixel(x, y)

# Write a frown face
for i in range(0,8):
  grid.writeRowRaw(i, frown_bmp[i]) 
time.sleep(1)

# Write a neutral face
for i in range(0,8):
  grid.writeRowRaw(i, neutral_bmp[i]) 
time.sleep(1)
  
# Write a smiley face
for i in range(0,8):
  grid.writeRowRaw(i, smile_bmp[i]) 
time.sleep(1)