#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr
c1 = ColorSensor(INPUT_1)
c2 = ColorSensor(INPUT_2) # bcs apparently they have to be backwards...
c3 = ColorSensor(INPUT_3)#gyro = GyroSensor(INPUT_1)
c4 = ColorSensor(INPUT_4)


steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
# mediumMotor_Left = MediumMotor(OUTPUT_A)
mediumMotor = MediumMotor(OUTPUT_D)

while True:
    Lcurrent_RLI = colourLeft.reflected_light_intensity
    Rcurrent_RLI = colourRight.reflected_light_intensity
    print('1 {} 2 {} 3 {} 4 {} '.format(c1,c2,c3,c4), file = stderr)
