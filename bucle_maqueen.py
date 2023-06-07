from microbit import *
from Maqueen import*

robot=Maqueen()

x = 0

while x<1:
    robot.forward()
    microbit.sleep(500)
    robot.motor_stop_all()
    x= x + 1
