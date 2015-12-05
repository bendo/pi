#!/usr/bin/env python3

import unicornhat as uh
import time
from random import randrange

uh.brightness(0.1)
uh.rotation(270)

while True:
    r = randrange(200, 255, 1)
    b = randrange(0, 200, 1)

    x = (r, 0, b)
    o = (0, 0, 0)

    heart = [
        [o,o,o,o,o,o,o,o],
        [o,x,x,o,o,x,x,o],
        [x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x],
        [o,x,x,x,x,x,x,o],
        [o,o,x,x,x,x,o,o],
        [o,o,o,x,x,o,o,o],
        [o,o,o,o,o,o,o,o]
        ]

    uh.set_pixels(heart)
    uh.show()
    time.sleep(0.5)
