#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

colourLeft = ColorSensor(INPUT_3) # bcs apparently they have to be backwards...
colourRight = ColorSensor(INPUT_2)
gyro = GyroSensor(INPUT_1)

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
# mediumMotor_Left = MediumMotor(OUTPUT_A)
mediumMotor = MediumMotor(OUTPUT_D)

def Turn_degrees(stop, speed, degrees):
    print("In Turn_degrees", file=stderr)
    current_gyro_reading = gyro.angle
    
    if degrees < 0:
        while current_gyro_reading>degrees:
            current_gyro_reading = gyro.angle
            tank_block.on(right_speed = speed, left_speed = -speed)
            if stop():
                break

    if degrees > 0:
        while current_gyro_reading < degrees:
            current_gyro_reading = gyro.angle
            tank_block.on(right_speed = -speed, left_speed = speed)
            if stop():
                break

    tank_block.off