#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.button import Button
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr
import os
from ev3dev2.sound import Sound

sound = Sound()
button = Button()
colourAttachment = ColorSensor(INPUT_4)
colourLeft = ColorSensor(INPUT_3) 
colourRight = ColorSensor(INPUT_2)
gyro = GyroSensor(INPUT_1)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
mediumMotor = MediumMotor(OUTPUT_D)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)
#_________________________________________________________________________________________________________________________________

# this is a program that we do not use that we where testing inbtween nregionals and nationals
while True:
    x = 0
    r = 0
    g = 0
    b = 0
    while True:
        button.wait_for_pressed(['enter'])
        rgb = colourAttachment.raw
        print(rgb, file=stderr)
        x = x + 1
        r = r + rgb[0]
        g = g + rgb[1]
        b = b + rgb[2]
        if x == 5:
            r = int(r/5)
            g = int(g/5)
            b = int(b/5)
            print('average was: {}, {}, {}'.format(r, g, b), file=stderr)
            print('new area', file = stderr)
            break