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
#_________________________________________________________________________________________________________________________________

def BlackLine_rotations(stop, speed, rotations, sensor, lineSide, correction):
    print("In BlackLine_rotations", file=stderr)
    # calculate how far to drive in degrees
    rotations = rotations*360
    # saves the current positions of the motors
    currentDegrees_left = largeMotor_Left.position
    currentDegrees_right = largeMotor_Right.position
    # calculates the target rotations for each motor
    target_left = currentDegrees_left + rotations
    target_right = currentDegrees_right + rotations
    # saves the current RLI for each sensor 
    right_RLI = colourRight.reflected_light_intensity
    left_RLI = colourLeft.reflected_light_intensity
    # RLI it should be reading if following the line
    target_RLI = 40

    if sensor == "RIGHT": # if using the right sensor 
        if lineSide == "LEFT": # if on left side of the line
            while currentDegrees_left < target_left: 
                # saves current motor position and RLI
                currentDegrees_left = largeMotor_Left.position
                right_RLI = colourRight.reflected_light_intensity
                # calulate the error
                error = right_RLI - target_RLI
                steering = 0
                
                # if on a low speed
                if speed < 12:
                    # use the appropriate steering depending on the error amount
                    if abs(error) < 5:
                        steering = error * 0.2
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.5
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 1
                    elif abs(error) >= 25:
                        steering = error * 1.25
                # if on a higher speedd
                if speed >= 12:
                    # use the appropriate steering depending on the error amount
                    if abs(error) < 5:
                        steering = error * 0.1
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.3
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 0.8
                    elif abs(error) >= 25:
                        steering = error * 1
                steering_drive.on(speed=speed, steering = steering)

                # if stop is True then exit the function
                if stop():
                    break

                sleep(0.01)
        # if on the right side of the lien
        elif lineSide == "RIGHT":
            while currentDegrees_left < target_left and currentDegrees_right < target_right:
                # saves the current motor posoitions and RLI 
                currentDegrees_left = largeMotor_Left.position
                currentDegrees_right = largeMotor_Right.position
                right_RLI = colourRight.reflected_light_intensity
                # calculates the error
                error = target_RLI - right_RLI
                steering = 0

                # if on a low speed
                if speed < 12:
                    # use the appropriate steering depending on the error
                    if abs(error) < 5:
                        steering = error * 0.2
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.5
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 1
                    elif abs(error) >= 25:
                        steering = error * 1.25
                # if on a higher speed
                if speed >= 12:
                    # use the appropriate steering depending on the error
                    if abs(error) < 5:
                        steering = error * 0.1
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.3
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 0.8
                    elif abs(error) >= 25:
                        steering = error * 1
                steering_drive.on(speed=speed, steering = steering)
                
                # if stop is true then exit the function
                if stop():
                    break
    
    # if the left sensor 
    elif sensor == "LEFT":
        # if following the right side of the lien
        if lineSide == "RIGHT":
            while currentDegrees_left < target_left and currentDegrees_right < target_right:
                # saves the motor positions and the current RLI
                currentDegrees_left = largeMotor_Left.position
                currentDegrees_right = largeMotor_Right.position
                left_RLI = colourLeft.reflected_light_intensity
                # calculates the error 
                error = target_RLI - right_RLI 
                steering = 0

                # if using a lower speed
                if speed < 12:
                    # use the appropriate steering depending on the error amount
                    if abs(error) < 5:
                        steering = error * 0.2
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.5
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 1
                    elif abs(error) >= 25:
                        steering = error * 1.25
                # if using a higher speed
                if speed >= 12:
                    # use the appropriate steering depending on the error amount
                    if abs(error) < 5:
                        steering = error * 0.1
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.3
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 0.8
                    elif abs(error) >= 25:
                        steering = error * 1
                steering_drive.on(speed=speed, steering = steering)
                # if stop is true then exit the function
                if stop():
                    break
        # if following the left side of the lien
        elif lineSide == "LEFT":
            while currentDegrees_left < target_left and currentDegrees_right < target_right:
                # saves the motor position and RLI
                currentDegrees_left = largeMotor_Left.position
                currentDegrees_right = largeMotor_Right.position
                left_RLI = colourLeft.reflected_light_intensity
                # calculates the error
                error = left_RLI - target_RLI 
                steering = 0

                # if the speed is lower 
                if speed < 12:
                    # use the appropriate steering depending on the error
                    if abs(error) < 5:
                        steering = error * 0.2
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.5
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 1
                    elif abs(error) >= 25:
                        steering = error * 1.25
                # if the speed is highger
                if speed >= 12:
                    # use the appropriate steering depending on the error
                    if abs(error) < 5:
                        steering = error * 0.1
                    elif abs(error) >= 5 and abs(error) <=10:
                        steering = error * 0.3
                    elif abs(error) >= 10 and abs(error) <=25:
                        steering = error * 0.8
                    elif abs(error) >= 25:
                        steering = error * 1
                steering_drive.on(speed=speed, steering = steering)
                # if stop is true then exit the function
                if stop():
                    break
    steering_drive.off()
    print("Leaving BlackLine_rotations", file=stderr)
