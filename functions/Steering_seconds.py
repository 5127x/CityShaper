#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

colourLeft = ColorSensor(INPUT_3)
colourRight = ColorSensor(INPUT_2)
gyro = GyroSensor(INPUT_1)
mediumMotor = MediumMotor(OUTPUT_D)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
#_________________________________________________________________________________________________________________________________


def Steering_seconds(stop, speed, seconds, steering): 
    print("In Steering_seconds", file=stderr)
    start_time = time.time()
    steering_drive.on(steering=steering, speed=speed)

    while time.time() < start_time + seconds:
        if stop():
            break
    steering_drive.off()
    print('Leaving Steering_seconds', file=stderr)

#stopProcessing=False
#Steering_seconds(lambda:stopProcessing, speed=30, seconds=3, steering=0)