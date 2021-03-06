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
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)

tank_block = MoveTank(OUTPUT_B, OUTPUT_C)
#_________________________________________________________________________________________________________________________________
def StraightGyro_target(stop, speed, rotations, target):
    print("In StraightGyro_target", file=stderr)
    current_degrees = largeMotor_Left.position 
    rotations = rotations * 360
    target_rotations= current_degrees + rotations
    current_gyro_reading = gyro.angle
    # print("Current Gyro Reading: {}".format(current_gyro_reading))
    while float(current_degrees) < target_rotations:
        if stop(): 
            break

        # reading in current gyro and  rotations
        current_gyro_reading=gyro.angle
        current_degrees = largeMotor_Left.position

        #if the gyro is smaller than the target
        if current_gyro_reading < target:
            correction = target - current_gyro_reading # calculate full error by target - gyro
            correction = correction * .25 # 1/4 of the correction (so the robot doesn't over correct)
            steering_drive.on(steering = -correction , speed = speed) # turn by the correctuion and doesn't over correct

        #if the gyro is larger than the target
        if current_gyro_reading > target:
            correction = target - current_gyro_reading # calculate full error by target - gyro
            correction = correction * .25  # 1/4 of the correction (so the robot doesn't over correct)
            steering_drive.on(steering = -correction , speed = speed) # turn by the correctuion and doesn't over correct

        #if the gyro is == to the target just go straight
        if current_gyro_reading == target:
            steering_drive.on(steering = 0 , speed = speed)

        # if the current rotations is larger than the target then break the loop which will stop the robot
        if float(current_degrees) >= target_rotations:
            break

        if stop():
            break

    tank_block.off()
    print('Leaving StraightGyro_target', file=stderr)

#stopProcessing=False
#StraightGyro_target(lambda:stopProcessing, speed=30, rotations=3)