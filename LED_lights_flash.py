from microbit import *
import music


while True:
    pin8.write_digital(1)
    pin12.write_digital(0)
    music.play(music.DADADADUM, pin=pin0, wait=True)
    sleep(2000)
    pin8.write_digital(0)
    pin12.write_digital(1)
    music.play(music.DADADADUM, pin=pin0, wait=True)
    sleep(2000)