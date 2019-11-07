#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from time import sleep
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
    print("In BlackLine_rotations", file=stderr)
    rotations = rotations*360
    currentDegrees_left = largeMotor_Left.position
    currentDegrees_right = largeMotor_Right.position
    target_left = currentDegrees_left + rotations
    target_right = currentDegrees_right + rotations
    right_RLI = colourRight.reflected_light_intensity
    left_RLI = colourLeft.reflected_light_intensity
    target_RLI = 40
    
    if sensor == "RIGHT":
        if lineSide == "LEFT":
            while currentDegrees_left < target_left: 
                #and currentDegrees_right < target_right:
                currentDegrees_left = largeMotor_Left.position
                #currentDegrees_right = largeMotor_Right.position
                right_RLI = colourRight.reflected_light_intensity
                error = right_RLI - target_RLI
                steering = 0
                if speed < 12:
                    if abs(error) < 5:
                        steering = error * 0.2
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.5
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 1
                    elif abs(error) >= 25:
                        steering = error * 1.25
                if speed >= 12:
                    if abs(error) < 5:
                        steering = error * 0.1
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.3
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 0.8
                    elif abs(error) >= 25:
                        steering = error * 1
                steering_drive.on(speed=speed, steering = steering)
                if stop():
                    break
                sleep(0.01)
        elif lineSide == "RIGHT":
            while currentDegrees_left < target_left and currentDegrees_right < target_right:
                currentDegrees_left = largeMotor_Left.position
                currentDegrees_right = largeMotor_Right.position
                right_RLI = colourRight.reflected_light_intensity
                error = target_RLI - right_RLI
                steering = 0
                if speed < 12:
                    if abs(error) < 5:
                        steering = error * 0.2
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.5
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 1
                    elif abs(error) >= 25:
                        steering = error * 1.25
                if speed >= 12:
                    if abs(error) < 5:
                        steering = error * 0.1
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.3
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 0.8
                    elif abs(error) >= 25:
                        steering = error * 1
                steering_drive.on(speed=speed, steering = steering)
                if stop():
                    break

    elif sensor == "LEFT":
        if lineSide == "RIGHT":
            while currentDegrees_left < target_left and currentDegrees_right < target_right:
                currentDegrees_left = largeMotor_Left.position
                currentDegrees_right = largeMotor_Right.position
                left_RLI = colourLeft.reflected_light_intensity
                error = target_RLI - right_RLI 
                steering = 0
                if speed < 12:
                    if abs(error) < 5:
                        steering = error * 0.2
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.5
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 1
                    elif abs(error) >= 25:
                        steering = error * 1.25
                if speed >= 12:
                    if abs(error) < 5:
                        steering = error * 0.1
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.3
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 0.8
                    elif abs(error) >= 25:
                        steering = error * 1
                steering_drive.on(speed=speed, steering = steering)
                if stop():
                    break
        elif lineSide == "LEFT":
            while currentDegrees_left < target_left and currentDegrees_right < target_right:
                currentDegrees_left = largeMotor_Left.position
                currentDegrees_right = largeMotor_Right.position
                left_RLI = colourLeft.reflected_light_intensity
                error = left_RLI - target_RLI 
                steering = 0
                if speed < 12:
                    if abs(error) < 5:
                        steering = error * 0.2
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.5
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 1
                    elif abs(error) >= 25:
                        steering = error * 1.25
                if speed >= 12:
                    if abs(error) < 5:
                        steering = error * 0.1
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.3
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 0.8
                    elif abs(error) >= 25:
                        steering = error * 1
                steering_drive.on(speed=speed, steering = steering)
                if stop():
                    break
    steering_drive.off()
    print("Leaving BlackLine_rotations", file=stderr)
'''
stopProcessing = False
BlackLine_rotations(lambda:stopProcessing, 10, 15, "RIGHT", "LEFT", 0.8)
'''