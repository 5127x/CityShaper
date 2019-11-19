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
gyro = GyroSensor(INPUT_1)

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
# mediumMotor_Left = MediumMotor(OUTPUT_A)
mediumMotor = MediumMotor(OUTPUT_D)

def Motor_onForSeconds(stop, motor, speed, seconds):
    print("In Motor_onForSeconds", file=stderr)
    # turn motor on for a number of seconds
    start_time = time.time()
    motor.on(speed=speed)  # turn the motor on forever
    while time.time() < start_time + seconds: # while the current time is smaller than the number of seconds
        if stop():
            break
    #Once completed turn the motor off
    motor.off()
    print('Leaving Motor_onForSeconds', file=stderr)

#stopProcessing=False
#Motor_onForSeconds(lambda:stopProcessing, motor=mediumMotor, speed=30, seconds=3)