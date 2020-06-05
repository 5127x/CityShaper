#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
colourLeft = ColorSensor(INPUT_2)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)

target_RLI = 40

while True:
    current_RLI = colourLeft.reflected_light_intensity
    error = current_RLI - target_RLI
    steering = (error * 0.175)#error * correction
    steering_drive.on(speed=22,steering = steering)
