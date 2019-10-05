#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time

colourAttachment = ColorSensor(INPUT_4)
colourLeft = ColorSensor(INPUT_2)
colourRight = ColorSensor(INPUT_3)
gyro = GyroSensor(INPUT_1)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
#mediumMotor_Left = MediumMotor(OUTPUT_A)
mediumMotor = MediumMotor(OUTPUT_D)

def Steering_seconds(stop, speed, seconds, steering, brake): 
    start_time = time.time()
    steering_drive.on(speed, brake = brake, block = False)
    while time.time() < start_time + seconds:
        if stop():
            break
    steering_drive.off()