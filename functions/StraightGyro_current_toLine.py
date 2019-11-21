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

#_________________________________________________________________________________________________________________________________

def StraightGyro_current_toLine(stop, speed, rotations, whiteOrBlack):

    print("In StraightGyro_current_toLine", file=stderr)
    
    current_degrees = largeMotor_Left.position 
    rotations = rotations * 360
    target_rotations= current_degrees + rotations
    target = gyro.angle
    current_gyro_reading = target

    # print("Current Gyro Reading: {}".format(current_gyro_reading))
    while float(current_degrees) < target_rotations: # if the current rotations is smaller than the target rotations
        if stop(): 
            break
        current_gyro_reading=gyro.angle #reading in gyro angle into the variable
        current_degrees = largeMotor_Left.position # reading in current rotations into as variable
        #if the gyro reading is smaller bc of the target rotations
        if current_gyro_reading < target:
            correction = target - current_gyro_reading # find the correction by target- current which will give you the error
            correction = correction * .25 # get a 1/4 of the error which is now the correction
            steering_drive.on(steering = -correction , speed = speed) # put correction into the steering block

        if current_gyro_reading > target:
            correction = target - current_gyro_reading # find the correction by target- current which will give you the error
            correction = correction * .25# get a 1/4 of the error which is now the correction
            steering_drive.on(steering = -correction , speed = speed) # put correction into the steering block

        if current_gyro_reading == target: # if the gyro reading is = to the target 
            steering_drive.on(steering = 0 , speed = speed) #then go straight

        if float(current_degrees) >= target_rotations: # if the current rotations is larger of = to the target rotations THEN BREAK THE LOOP
            break
        if stop():
            break

    # Now find the line
    
    if not stop(): # if the robot has not stopped
        while True:
            if stop(): 
                break
            # read RLI values into variables
            currentRight_RLI = colourRight.reflected_light_intensity
            currentLeft_RLI = colourLeft.reflected_light_intensity
            #Go forward but half the speed (allows the line to be found easier)
            steering_drive.on(steering = 0 , speed = speed / 2)

            if whiteOrBlack == "WHITE": # if the line your looking for is White
                if currentRight_RLI > 65 or currentLeft_RLI > 65: #look if either colour sensor value is larger than 65 then break
                    break

            if whiteOrBlack == "BLACK": # if the line your looking for is Black
                if currentRight_RLI < 10 or currentLeft_RLI < 10:#look if either colour sensor value is smaller then 10 then break
                    break

    tank_block.off()
    print('Leaving StraightGyro_current_toLine', file=stderr)

#stopProcessing=False
#StraightGyro_current(lambda:stopProcessing, speed=30, rotations=3)