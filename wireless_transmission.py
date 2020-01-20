from microbit import *
import radio


radio.on()
radio.config(channel=7)

while True:
    if button_a.is_pressed():
        radio.send("A")
        display.scroll(str("A"), wait=False, loop=False)
    if button_b.is_pressed():
        radio.send("B")
        display.scroll(str("B"), wait=False, loop=False)