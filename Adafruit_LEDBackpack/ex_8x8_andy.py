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
    # time.sleep(0.5)
# Continually update the 8x8 display one pixel at a time
# while(True):
#   iter += 1

#   for x in range(0, 8):
#     for y in range(0, 8):
#       grid.setPixel(x, y, iter % 4 )
#       time.sleep(0.02)
