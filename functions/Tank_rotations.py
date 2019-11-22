#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

tank_block = MoveTank(OUTPUT_B, OUTPUT_C)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
#_________________________________________________________________________________________________________________________________
def Tank_rotations(stop, left_speed, right_speed, rotations):
    print("In Tank_rotations", file=stderr)
    # create left target rotations
    current_degrees_left = largeMotor_Left.position 
    target_left = rotations * 360
    if left_speed < 0: 
        target_left= -target_left
    target_left= target_left+current_degrees_left

    # create right target rtations
    current_degrees_right = largeMotor_Right.position
    target_right = rotations * 360
    if right_speed < 0: 
        target_right = target_right
    target_right=target_right+current_degrees_right
    # turn the motors on until either motor reaches it's target rotations
    tank_block.on(right_speed=right_speed, left_speed=left_speed)


    if current_degrees_left < target_left and current_degrees_right < target_right: # if the current rotations of a specific motor is smaller than the target rotations of a specific motor
        while current_degrees_left < target_left or current_degrees_right < target_right: # how its done in tank onForRotations
            # reading in the values for currenrt readings (current rotations)
            current_degrees_left = largeMotor_Left.position 
            current_degrees_right = largeMotor_Right.position
            if stop():
                break
            if current_degrees_left >= target_left or current_degrees_right >= target_right:
                break
    
    elif current_degrees_left < target_left and current_degrees_right > target_right:
        #print("2", file=stderr)
        while current_degrees_left < target_left or current_degrees_right > target_right: # how its done in tank onForRotations
            # reading in the values for currenrt readings (current rotations)
            current_degrees_left = largeMotor_Left.position 
            current_degrees_right = largeMotor_Right.position
            if stop():
                break
            if current_degrees_left >= target_left or current_degrees_right <= target_right:
                break
    
    elif current_degrees_left > target_left and current_degrees_right < target_right:
        #print("3", file=stderr
        while current_degrees_left > target_left or current_degrees_right < target_right: # how its done in tank onForRotations
            # reading in the values for currenrt readings (current rotations)
            current_degrees_left = largeMotor_Left.position 
            current_degrees_right = largeMotor_Right.position
            if stop():
                break
            if current_degrees_left <= target_left or current_degrees_right >= target_right:
                break
    
    elif current_degrees_left > target_left and current_degrees_right > target_right:
        #print("4", file=stderr)
        while current_degrees_left > target_left or current_degrees_right > target_right: # how its done in tank onForRotations
            # reading in the values for currenrt readings (current rotations)
            current_degrees_left = largeMotor_Left.position 
            current_degrees_right = largeMotor_Right.position
            
            if stop():
                break
            if current_degrees_left <= target_left or current_degrees_right <= target_right:
                break
    tank_block.off()
    print('Leaving Tank_rotations', file=stderr)

#stopProcessing=False
#Tank_rotations(lambda:stopProcessing, left_speed=30, right_speed=30, rotations=5)