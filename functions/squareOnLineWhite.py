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

def squareOnLineWhite(stop, speed, target):
    print("In squareOnLine", file=stderr)
    # setting colour sensors and bool variable
    colourLeft_RLI = 0
    colourRight_RLI = 0
    lineFound = False
    # turning on motor
    steering_drive.on(steering=0,speed=speed)
    while True:
        colourLeft_RLI = colourLeft.reflected_light_intensity
        colourRight_RLI = colourRight.reflected_light_intensity
        
        #if the left RLU is larger than the target
        if colourLeft_RLI >= target:
            largeMotor_Left.on(-speed/2) # left motor goes back 1/2 of the original speed
            largeMotor_Right.on(speed) # right sensor goes forward
            lineFound = True # set line found to True
            print('{} left found it'.format(colourLeft_RLI), file = stderr) # printing info on laptop

        #if the left RLU is larger than the target
        if colourRight_RLI >=target:
            largeMotor_Left.on(speed)# right sensor goes forward
            largeMotor_Right.on(-speed/2)# right motor goes back 1/2 of the original speed
            lineFound = True # set line found to True
            print('{} right found it'.format(colourRight_RLI), file = stderr)

        print('{} left, {} right'.format(colourLeft_RLI, colourRight_RLI), file = stderr)
    
        if abs(colourLeft_RLI - colourRight_RLI) < 20 and lineFound:
            break
        if stop():
            break
    steering_drive.off()
    print('Leaving squareOnLine', file=stderr)

#stopProcessing=False
#squareOnLine(lambda:stopProcessing, speed=30, target=100)