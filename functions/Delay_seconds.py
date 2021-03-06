#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

# Defining ports
colourLeft = ColorSensor(INPUT_3) 
colourRight = ColorSensor(INPUT_2)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
mediumMotor = MediumMotor(OUTPUT_D)
#_________________________________________________________________________________________________________________________________

def Delay_seconds(stop, seconds):
    # wait for a certain number of seconds
    print("In Delay_seconds", file=stderr)
    start_time = time.time()
    while time.time() < start_time + seconds:
        if stop():
            break
    print('Leaving Delay_seconds', file=stderr)

