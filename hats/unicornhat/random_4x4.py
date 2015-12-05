#!/usr/bin/env python3

import unicornhat as uh
import time
from random import randrange

while True:    
    x = randrange(2,6,1)
    y = randrange(2,6,1)
    r = randrange(0,255,1)
    g = randrange(0,255,1)
    b = randrange(0,255,1)
    br = randrange(5,10,1)

    uh.rotation(270)
    uh.brightness(br/100)
    uh.set_pixel(x, y, r, g, b)
    uh.show()

    time.sleep(0.2)
