#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr
#from LookingBlackLine_stopBlack import LookingBlackLine_stopBlack
from FollowBlackLine_rotations import FollowBlackLine_rotations
from LookingBlackLine_rotations import FollowBlackLine_rotations

'''
from onForRotations import onForRotations
from tank_rotations import tank_rotations
from Degrees_aim import turn_to_degrees
from Delay_seconds import Delay_seconds
from reset_gyro import reset_gyro
'''
colourAttachment = ColorSensor(INPUT_4)

colourLeft = ColorSensor(INPUT_3) # bcs apparently they have to be backwards...
colourRight = ColorSensor(INPUT_2)
gyro = GyroSensor(INPUT_1)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
# mediumMotor_Left ]\
# = MediumMotor(OUTPUT_A)
mediumMotor = MediumMotor(OUTPUT_D)

FollowBlackLine_rotations(speed= 10, rotations = 5, colourSensor= "RIGHT", lineSide = "LEFT", stop = False )

#RIGHT = 4423q  
#turn_to_degrees(lambda:stopProcessing, speed=20, degrees=90) # speeds over 5 are inaccurate but still get more or less right (to be fair, they are inaccurate by the same amount each time...)
#Delay_seconds(lambda:stopProcessing, 2)8 
#turn_to_degrees(lambda:stopProcessing, speed=5, degrees=90) # second time at slow speed for accuracy
#tank_rotations(lambda:stopProcessing, left_speed=30, right_speed=20, rotations=0.6 )
#onForRotations(lambda:stopProcessing, motor=mediumMotor, speed=-30, rotations=-0.2, gearRatio=1.4)