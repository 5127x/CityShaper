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
#gyro = GyroSensor(INPUT_1)


steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
# mediumMotor_Left = MediumMotor(OUTPUT_A)
mediumMotor = MediumMotor(OUTPUT_D)

def onForRotations(stop, motor, speed, rotations, gearRatio): 
    print("In onForRotations", file=stderr)
    current_degrees = motor.position # there isnt a way to read rotations
    rotations = rotations*gearRatio
    target_rotations = rotations * 360 # convert to degrees bcs its simpler
    target_rotations = current_degrees + target_rotations
    # if speed == 0: 
    # target_rotations = - target_rotations
    motor.on(speed=speed)
    if current_degrees > target_rotations:
        while current_degrees > target_rotations:
            current_degrees = motor.position
            if stop():
                break
            if current_degrees <= target_rotations:
                break
    elif current_degrees < target_rotations:
        while current_degrees < target_rotations:
            current_degrees = motor.position
            if stop():
                break
            if current_degrees >= target_rotations:
                break
    motor.off()
    print('Leaving onForRotations', file=stderr)

#stopProcessing=False
#onForRotations(lambda:stopProcessing, motor=mediumMotor, speed=30, rotations=2, gearRatio=1.4)