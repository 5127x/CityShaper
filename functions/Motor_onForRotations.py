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
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
mediumMotor = MediumMotor(OUTPUT_D)

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)z

#_________________________________________________________________________________________________________________________________

def Motor_onForRotations(stop, motor, speed, rotations, gearRatio): 
    print("In onForRotations", file=stderr)
    # read the motor position (degrees since there isn't a way to read rotations)
    current_degrees = motor.position 
    # take the gearRatio into account
    rotations = rotations*gearRatio
    # create target rotations
    target_rotations = rotations * 360
    target_rotations = current_degrees + target_rotations
    # turn the motor on until current_degrees matches target_rotations
    motor.on(speed=speed)
    
    # Just a note. The larger and smaller is because if the robot is going backward. 
    
    if current_degrees > target_rotations:# current degrees can also be how many rotations a motor has done
        while current_degrees > target_rotations: # while current rotations is larger than target
            current_degrees = motor.position # reading current rotations into the paramater
            # continue speed until one of the following staements become true
            if stop():
                break
            if current_degrees <= target_rotations:
                break

    elif current_degrees < target_rotations:
        while current_degrees < target_rotations: # while current rotations is smaller than target
            current_degrees = motor.position # reading current rotations into the paramater
            # continue speed until one of the following staements become true
            if stop():
                break
            if current_degrees >= target_rotations:
                break
    motor.off()
    print('Leaving onForRotations', file=stderr)

#stopProcessing=False
#Motor_onForRotations(lambda:stopProcessing, motor=mediumMotor, speed=30, rotations=2, gearRatio=1.4)