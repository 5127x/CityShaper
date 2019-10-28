#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

colourAttachment = ColorSensor(INPUT_4)
colourLeft = ColorSensor(INPUT_3) 
colourRight = ColorSensor(INPUT_2)
gyro = GyroSensor(INPUT_1)

largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
mediumMotor = MediumMotor(OUTPUT_D)

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

def BlackLine_rotations(stop, speed, rotations, sensor, lineSide, correction):
    rotations = rotations*360
    currentDegrees_left = largeMotor_Left.position
    currentDegrees_right = largeMotor_Right.position
    target_left = currentDegrees_left + rotations
    target_right = currentDegrees_right + rotations
    right_RLI = colourRight.reflected_light_intensity
    left_RLI = colourLeft.reflected_light_intensity
    target_RLI = 40
    
    while currentDegrees_left < target_left and currentDegrees_right < target_right:
        currentDegrees_left = largeMotor_Left.position
        currentDegrees_right = largeMotor_Right.position
        if sensor == "RIGHT":
            if lineSide == "LEFT":
                right_RLI = colourRight.reflected_light_intensity
                target_RLI = 40
                correctiom = correction
                right_RLI = colourRight.reflected_light_intensity
                error = right_RLI - target_RLI
                steering = error * correction
                steering_drive.on(speed=speed, steering = steering)
            elif lineSide == "RIGHT":
                right_RLI = colourRight.reflected_light_intensity
                target_RLI = 40
                correctiom = correction
                right_RLI = colourRight.reflected_light_intensity
                error = target_RLI - right_RLI
                steering = error * correction
                steering_drive.on(speed=speed, steering = steering)

        elif sensor == "LEFT":
            if lineSide == "RIGHT":
                target_RLI = 40
                correctiom = correction
                left_RLI = colourLeft.reflected_light_intensity
                error = target_RLI - right_RLI 
                steering = error * correction
                steering_drive.on(speed=speed, steering = steering)
            elif lineSide == "LEFT":
                target_RLI = 40
                correctiom = correction
                left_RLI = colourLeft.reflected_light_intensity
                error = left_RLI - target_RLI 
                steering = error * correction
                steering_drive.on(speed=speed, steering = steering)
        
        if stop():
            break
    steering_drive.off()
'''
print('hi...............')
stopProcessing = False
BlackLine_rotations(lambda:stopProcessing, 10, 15, "LEFT", "LEFT", 1.5)
'''
