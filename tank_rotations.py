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

def tank_rotations(stop, left_speed, right_speed, rotations): # needs to be changed to work with - and + speeds (Test other function)
    print("In tank_rotations", file=stderr)
    current_degrees_left = largeMotor_Left.position # there isnt a way to read rotations
    current_degrees_right = largeMotor_Right.position
    target_rotations = rotations * 360 # convert to degrees bcs its simpler
    target_rotations_left = current_degrees_left + target_rotations
    target_rotations_right = current_degrees_right + target_rotations

    tank_block.on(right_speed=right_speed, left_speed=left_speed)
    while current_degrees_left < target_rotations_left or current_degrees_right < target_rotations_right: # how its done in tank onForRotations
        current_degrees_left = largeMotor_Left.position 
        current_degrees_right = largeMotor_Right.position
        if stop():
            break
        if current_degrees_left >= target_rotations_left or current_degrees_right >= target_rotations_right:
            break
    tank_block.off()