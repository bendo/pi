#!/usr/bin/env python3

import unicornhat as uh
import time

uh.brightness(0.2)

for x in range(7,-1,-1):
    uh.set_pixel(x, 7-x, 255, 255, 0)
    uh.show()
    time.sleep(0.1)

time.sleep(10)
