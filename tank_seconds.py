#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

tank_block = MoveTank(OUTPUT_B, OUTPUT_C)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)

def Tank_seconds(stop, left_speed, right_speed, seconds): 
    # turn the motors on for a number of seconds
    print("In tank_seconds", file=stderr)
    start_time = time.time()
    tank_block.on(right_speed=right_speed, left_speed=left_speed)
    while time.time() < start_time + seconds:
        if stop():
            break
    tank_block.off()
    print('Leaving Tank_seconds', file=stderr)

#stopProcessing=False
#Tank_seconds(lambda:stopProcessing, left_speed=30, right_speed=30, rotations=5)