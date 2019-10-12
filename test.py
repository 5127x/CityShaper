#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr
from onForRotations import onForRotations
colourLeft = ColorSensor(INPUT_3) # bcs apparently they have to be backwards...
colourRight = ColorSensor(INPUT_2)
gyro = GyroSensor(INPUT_1)

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
# mediumMotor_Left = MediumMotor(OUTPUT_A)
mediumMotor = MediumMotor(OUTPUT_D)

colourAttachment = ColorSensor(INPUT_4)
stopProcessing=False
onForRotations(lambda:stopProcessing, motor=mediumMotor, speed=-60, rotations=-0.5, gearRatio=1.4 )
'''
onForRotations(lambda:stopProcessing, motor=mediumMotor, speed=60, rotations=0.3, gearRatio=1.4 )
onForRotations(lambda:stopProcessing, motor=mediumMotor, speed=-60, rotations=-0.4, gearRatio=1.4 )
onForRotations(lambda:stopProcessing, motor=mediumMotor, speed=60, rotations=1, gearRatio=1.4 )
'''