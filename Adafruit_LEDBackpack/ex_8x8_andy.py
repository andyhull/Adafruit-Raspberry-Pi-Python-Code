#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import ColorEightByEight

# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
grid = ColorEightByEight(address=0x70)

print "Press CTRL+Z to exit"

iter = 0
# grid.setPixel(1, 1)
# time.sleep(0.5)
for x in range(1, 4):
  for y in range(1, 4):
    grid.setPixel(x, y)

# Write a smiley face
for i in range(0,8):
  grid.writeRowRaw(i, smile_bmp[i]) 
time.sleep(.33)

# Write a neutral face
for i in range(0,8):
  grid.writeRowRaw(i, neutral_bmp[i]) 
time.sleep(.33)
  
# Write a frown face
for i in range(0,8):
  grid.writeRowRaw(i, frown_bmp[i]) 
time.sleep(.33)
