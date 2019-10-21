#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

gyro = GyroSensor(INPUT_1)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

def Turn_degrees(stop, speed, degrees): 
    # create the target degrees
    print("In Turn_degrees", file=stderr)
    current_gyro_reading = gyro.angle
    target_degrees = current_gyro_reading + degrees
    # turn until it has turned the needed degrees
    if current_gyro_reading > target_degrees:
        tank_block.on(right_speed = -speed, left_speed = speed)
        while current_gyro_reading > target_degrees:
            current_gyro_reading = gyro.angle
            if stop():
                break

    elif current_gyro_reading < target_degrees:
        tank_block.on(right_speed = speed, left_speed = -speed)
        while current_gyro_reading < target_degrees:
            current_gyro_reading = gyro.angle
            if stop():
                break

    tank_block.off
    print('Leaving Turn_degrees', file= stderr)

#stopProcessing=False
#Turn_degrees(lambda:stopProcessing, speed=30, degrees=90)