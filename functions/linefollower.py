#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.button import Button
import xml.etree.ElementTree as ET
import threading
import time
from time import sleep
from sys import stderr
import os

button = Button()
colourAttachment = ColorSensor(INPUT_4)
colourLeft = ColorSensor(INPUT_3) 
colourRight = ColorSensor(INPUT_2)
gyro = GyroSensor(INPUT_1)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
mediumMotor = MediumMotor(OUTPUT_D)

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)
#_________________________________________________________________________________________________________________________________

def steering(course, power):
    power_left = power_right = power
    s = (50 - abs(float(course))) / 50
    if course >= 0:
        power_right = - power
    else:
        power_left *= 5
        if course < -100:
            power_left = - power
    return (int(power_left)), int(power_right)

def steering2(course, power):
    if course >= 0:
        if course > 100:
            power_right = 0
            power_left = power
        else:
            power_left = power
            power_right = power - ((power * course) / 100)
    else:
        if course <-100:
            power_left = 0
            power_right =power
        else:
            power_right = power
            power_left = power + ((power * course) / 100)
    return (int(power_left)), int(power_right)

def run(power, target, kp, ki, kd, direction, miniRef, maxRef):
    lastError = error = integral = 0
    largeMotor_Left.run_direct()
    largeMotor_Right.run_direct()
    while not button.any():
        refRead = colourRight.value()
        error = target - (100 * (refRead - miniRef) / (maxRef - miniRef))
        derivative = error - lastError
        integral = float(0.5) * integral + error
        course = (kp * error + kd * derivative + ki * integral) * direction
        for (motor, pow) in zip((largeMotor_Left, largeMotor_Right), steering2(course, power)):
            motor.duty_cycle_sp = pow
        sleep(0.01)

#run(50, 55, float(0.65), float(0.02), 1, 1, 40, 100)