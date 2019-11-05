#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

gyro = GyroSensor(INPUT_1)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)

colourLeft = ColorSensor(INPUT_3)
colourRight = ColorSensor(INPUT_2)


def StraightGyro_target_toLine(stop, speed, rotations, target, whiteOrBlack):

    print("In StraightGyro_target_toLine", file=stderr)
    current_degrees = largeMotor_Left.position 
    rotations = rotations * 360
    target_rotations= current_degrees + rotations
    current_gyro_reading = gyro.angle
    # print("Current Gyro Reading: {}"(current_gyro_reading))

    while float(current_degrees) < target_rotations:
        if stop(): 
            break
        current_gyro_reading = gyro.angle
        current_degrees = largeMotor_Left.position
        if current_gyro_reading < target:
            correction = target - current_gyro_reading
            correction = correction * .25
            steering_drive.on(steering = -correction , speed = speed)
        if current_gyro_reading > target:
            correction = target - current_gyro_reading
            correction = correction * .25
            steering_drive.on(steering = -correction , speed = speed)
        if current_gyro_reading == target:
            steering_drive.on(steering = 0 , speed = speed)
        if float(current_degrees) >= target_rotations:
            break
        if stop():
            break
    

    # Now find the line
    
    if not stop():
        while True:
            if stop(): 
                break
            currentRight_RLI = colourRight.reflected_light_intensity
            currentLeft_RLI = colourLeft.reflected_light_intensity

            if whiteOrBlack == "WHITE":
                if currentRight_RLI > 80 or currentLeft_RLI > 80:
                    break

            if whiteOrBlack == "BLACK":
                if currentRight_RLI < 10 or currentLeft_RLI < 10:
                    break
            steering_drive.on(steering = 0 , speed = speed / 2)                


    tank_block.off()
    print('Leaving StraightGyro_target_toLine', file=stderr)

#stopProcessing=False
#StraightGyro_target_toLine(lambda:stopProcessing, speed=30, rotations=3, target=45, whiteOrBlack="WHITE")