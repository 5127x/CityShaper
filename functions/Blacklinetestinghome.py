#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color

ev3 = EV3Brick()
colourLeft = ColorSensor(Port.S2)

steering_drive = steering.drive(Motor(Port.B), Motor(Port.C))

def testing_blackline (correction, speed):
    while True:
        cur_RLI = colourRight.reflected_light_intensity
        error = cur_RLI - 40
        steering = error * correction
        steering_drive.on(speed,steering)


testing_blackline (0.5, 5)

#!/usr/bin/env pybricks-micropython

import time
from sys import stderr
ev3 = EV3Brick()
colourLeft = ColorSensor(Port.S2)
def RLI_testing2():
    x=0
    start_time = time.time()
    while time.time() < start_time + 1:
        RLI = colourLeft.reflection()
        x = x+1
    print(x, file=stderr) 