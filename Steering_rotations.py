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

def Steering_rotations(stop, speed, rotations, steering):
    print("In Steering_rotations", file=stderr)
    current_degrees_left = largeMotor_Left.position # there isnt a way to read rotations
    current_degrees_right = largeMotor_Right.position
    target_rotations = rotations * 360 # convert to degrees bcs its simpler
    target_rotations_left = current_degrees_left + target_rotations
    target_rotations_right = current_degrees_right + target_rotations

    steering_drive.on(steering = steering, speed= speed)
    if current_degrees_left < target_left and current_degrees_right < target_right:
        #print("1", file=stderr)
        while current_degrees_left < target_left or current_degrees_right < target_right: # how its done in tank onForRotations
            current_degrees_left = largeMotor_Left.position 
            current_degrees_right = largeMotor_Right.position
            if stop():
                break
            if current_degrees_left >= target_left or current_degrees_right >= target_right:
                break
    # < >
    elif current_degrees_left < target_left and current_degrees_right > target_right:
        #print("2", file=stderr)
        while current_degrees_left < target_left or current_degrees_right > target_right: # how its done in tank onForRotations
            current_degrees_left = largeMotor_Left.position 
            current_degrees_right = largeMotor_Right.position
            if stop():
                break
            if current_degrees_left >= target_left or current_degrees_right <= target_right:
                break
    # > <
    elif current_degrees_left > target_left and current_degrees_right < target_right:
        #print("3", file=stderr)
        while current_degrees_left > target_left or current_degrees_right < target_right: # how its done in tank onForRotations
            current_degrees_left = largeMotor_Left.position 
            current_degrees_right = largeMotor_Right.position
            if stop():
                break
            if current_degrees_left <= target_left or current_degrees_right >= target_right:
                break
    # > > 
    elif current_degrees_left > target_left and current_degrees_right > target_right:
        #print("4", file=stderr)
        while current_degrees_left > target_left or current_degrees_right > target_right: # how its done in tank onForRotations
            current_degrees_left = largeMotor_Left.position 
            current_degrees_right = largeMotor_Right.position
            if stop():
                break
            if current_degrees_left <= target_left or current_degrees_right <= target_right:
                break
    steering_drive.off()
    print('Leaving Steering_rotations', file=stderr)

#stopProcessing=False
#squareOnLine(lambda:stopProcessing, speed=30, rotations=5, steering=0)