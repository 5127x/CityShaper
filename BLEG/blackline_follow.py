#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

colourRight = ColorSensor(INPUT_2)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)

def testing_blackline (correction, speed):
    while True:
        cur_RLI = colourRight.reflected_light_intensity
        error = cur_RLI - 40
        steering = error * correction
        steering_drive.on(speed,steering)


testing_blackline (0.5, 5)
