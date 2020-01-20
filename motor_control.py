from microbit import *
import maqueenMotor


motor = maqueenMotor()
while True:
    motor.run(0,0,200)
    motor.run(1,0,200)
    sleep(1000)
    motor.run(0,0,100)
    motor.run(1,0,0)
    sleep(1000)
    motor.run(0,0,200)
    motor.run(1,0,200)
    sleep(1000)
    motor.run(0,0,100)
    motor.run(1,0,0)
    sleep(1000)