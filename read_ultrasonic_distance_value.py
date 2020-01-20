from microbit import *
import urm10


while True:
    display.scroll(str(urm10.read(2, 1)), wait=False, loop=False)
    sleep(1000)