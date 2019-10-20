#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from sys import stderr
#steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
gyro = GyroSensor(INPUT_1)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)


def Turn_from_start_position(stop, speed, degrees):
    print("In Turn_from_start_position", file=stderr)
    current_gyro_reading = gyro.angle
    print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)

    if current_gyro_reading < degrees:
        tank_block.on(left_speed = -speed, right_speed = speed)
        while current_gyro_reading < degrees:
            #print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)                
            current_gyro_reading = gyro.angle
            if current_gyro_reading >= degrees:
                break
            if stop():
                break
    elif current_gyro_reading > degrees:
        tank_block.on(left_speed = speed, right_speed = -speed)
        while current_gyro_reading > degrees:
            #print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)                
            current_gyro_reading = gyro.angle
            if current_gyro_reading <= degrees:
                break
            if stop():
                break
    tank_block.off()
    print("Leaving Turn_from_start_position", file=stderr)        
    print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)

turn_to_degrees(stop = "FALSE", speed = 10, degrees = 90)
#stopProcessing=False
#Turn_from_start_position(lambda:stopProcessing, speed=30, degrees=90)