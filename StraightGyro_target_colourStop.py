#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

gyro = GyroSensor(INPUT_1)
colourLeft = ColorSensor(INPUT_3) 
colourRight = ColorSensor(INPUT_2)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)

def StraightGyro_target_colourStop(stop, speed, target, sensor, value):
    print("In StraightGyro_target", file=stderr)
    current_gyro_reading = gyro.angle
    # print("Current Gyro Reading: {}".format(current_gyro_reading))
    if sensor == 'LEFT':
        current_RLI = colourLeft.reflected_light_intensity
    elif sensor == 'RIGHT':
        current_RLI = colourRight.reflected_light_intensity

    while current_RLI > target_rotations:
        if stop(): 
            break
        current_gyro_reading=gyro.angle
        if sensor == 'LEFT':
            current_RLI = colourLeft.reflected_light_intensity
        elif sensor == 'RIGHT':
            current_RLI = colourRight.reflected_light_intensity

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
        if stop():
            break
    tank_block.off()
    print('Leaving StraightGyro_target', file=stderr)

#stopProcessing=False
#StraightGyro_target(lambda:stopProcessing, speed=30, rotations=3)