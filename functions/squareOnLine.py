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
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
mediumMotor = MediumMotor(OUTPUT_D)

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)
#_________________________________________________________________________________________________________________________________


def squareOnLine(stop, speed, target):
    print("In squareOnLine", file=stderr)
    # setting up program
    colourLeft_RLI = 0
    colourRight_RLI = 0
    lineFound = False
    #Turning on motor
    steering_drive.on(steering=0,speed=speed)
    while True:
        #reading in the colour sensor values (reflected light intensity)
        colourLeft_RLI = colourLeft.reflected_light_intensity
        colourRight_RLI = colourRight.reflected_light_intensity
        # if the left Rli is smaller than the target/aim then turn to the right
        if colourLeft_RLI <= target:
            largeMotor_Left.on(-speed)
            largeMotor_Right.on(speed)
            lineFound = True #setting bool varisable for cancelling movment later on
            print('{} left found it'.format(colourLeft_RLI), file = stderr)

        # if the right Rli is smaller than the target/aim then turn to the left
        if colourRight_RLI <=target:
            largeMotor_Left.on(speed)
            largeMotor_Right.on(-speed)
            lineFound = True #setting bool varisable for cancelling movment later on
            print('{} right found it'.format(colourRight_RLI), file = stderr)

        print('{} left, {} right'.format(colourLeft_RLI, colourRight_RLI), file = stderr)
    
        if colourLeft_RLI == colourRight_RLI and lineFound:
            break
        if stop():
            break
    steering_drive.off()
    print('Leaving squareOnLine', file=stderr)

#stopProcessing=False
#squareOnLine(lambda:stopProcessing, speed=30, target=100)