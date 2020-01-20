from microbit import *
import maqueenMotor
import urm10


motor = maqueenMotor()
while True:
    motor.run(0,0,200)
    motor.run(1,0,200)
    mind_n_Distance = urm10.read(2, 1)
    if (mind_n_Distance < 50):
        motor.run(0,0,0)
        motor.run(1,0,200)
        sleep(1000)