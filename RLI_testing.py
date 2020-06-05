#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import time
from sys import stderr

# Defining ports
colourLeft = ColorSensor(INPUT_3)
x=0
#_________________________________________________________________________________________________________________________________

start_time = time.time()
while time.time() < start_time + 1:
    RLI = colourLeft.reflected_light_intensity
    print(RLI, file=stderr)
    x = x+1
print(x, file=stderr)

