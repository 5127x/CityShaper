#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.button import Button
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr
import os
#from LookingBlackLine_stopBlack import LookingBlackLine_stopBlack
from FollowBlackLine_rotations import FollowBlackLine_rotations
from LookingBlackLine_rotations import LookingBlackLine_rotations

from Delay_seconds import Delay_seconds
'''
from onForRotations import onForRotations
from tank_rotations import tank_rotations
from Degrees_aim import turn_to_degrees
from reset_gyro import reset_gyro
'''
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
'''
colourAttachment = ColorSensor(INPUT_4)
'''
x=0 
stopProcessing=False
while True:
    print(x, file= stderr)
    print(colourAttachment.raw, file=stderr)
    x = x + 1
    Delay_seconds(lambda:stopProcessing, 5)
'''

def colourAttachment_values():
    button = Button()
    stop = False
    os.system('setfont Lat15-TerminusBold14')
    # os.system('setfont Lat15-TerminusBold32x16')  # Try this larger font

    print('insert black', file=stderr)
    print('insert black')
    button.wait_for_pressed(['enter'])
    black = colourAttachment.raw

    print('insert green', file=stderr)
    print('insert green')
    Delay_seconds(lambda:stop, 2)
    green = colourAttachment.raw

    print('insert red', file=stderr)
    print('insert red')
    Delay_seconds(lambda:stop, 2)
    red = colourAttachment.raw

    print('insert yellow', file=stderr)
    print('insert yellow')
    Delay_seconds(lambda:stop, 2)
    yellow = colourAttachment.raw

    print('insert white', file=stderr)
    print('insert white')
    Delay_seconds(lambda:stop, 2)
    white = colourAttachment.raw

    attachment_values = [black, green, red, yellow, white]
    print(black[0], file=stderr)
    return attachment_values

attachment_values = colourAttachment_values()
print('attachment_values: {}'.format(attachment_values))


'''

Sensor 1 = {nothing:(63, 66, 152)
            black:(31, 39, 78)
            red:(208, 54, 63)
            yellow:(307, 250, 105)
            white:(327, 401, 499)
            brown:(73, 56, 72)}

Sensor 2 = {nothing:(43, 44, 41)
            black:(22, 29, 24)
            red:(171, 36, 22)
            yellow:(264, 169, 44)
            white:(277, 273, 218)
            brown:(57, 35, 24)}

'''

#LookingBlackLine_rotations(speed= 18, rotations = 5, colourSensor= "RIGHT", Turning = .15,lineSide = "LEFT", stop = False )
#FollowBlackLine_rotations(speed= 10, rotations = 5, colourSensor= "RIGHT", lineSide = "LEFT", stop = False )
#RIGHT = 4423q  
#turn_to_degrees(lambda:stopProcessing, speed=20, degrees=90) # speeds over 5 are inaccurate but still get more or less right (to be fair, they are inaccurate by the same amount each time...)
#Delay_seconds(lambda:stopProcessing, 2)8 
#turn_to_degrees(lambda:stopProcessing, speed=5, degrees=90) # second time at slow speed for accuracy
#tank_rotations(lambda:stopProcessing, left_speed=30, right_speed=20, rotations=0.6 )
#onForRotations(lambda:stopProcessing, motor=mediumMotor, speed=-30, rotations=-0.2, gearRatio=1.4)