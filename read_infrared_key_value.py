from microbit import *
import necir

mind_n_P16 = 0

def IR_callback(IR_addr, IR_cmd):
    global mind_n_P16
    mind_n_P16 = IR_cmd
    display.scroll(str(mind_n_P16), wait=False, loop=False)


necir.init(16, IR_callback)

while True:
    pass