#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from sys import stderr
gyro = GyroSensor(INPUT_1)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

#_________________________________________________________________________________________________________________________________

def Turn_from_start_position(stop, speed, degrees):
    print("In Turn_from_start_position", file=stderr)
    current_gyro_reading = gyro.angle
    print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)

    # if the gyro is smaller than degrees (parameter from above)
    if current_gyro_reading < degrees:
        tank_block.on(left_speed = -speed, right_speed = speed) #turn the robot
        while current_gyro_reading < degrees:
            #print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)    
            # read in the gyro value            
            current_gyro_reading = gyro.angle
            #gyro reading is larger than target (once reached the degrees) stop program
            if current_gyro_reading >= degrees:
                break
            if stop():
                break

    # if the gyro is larger than degrees (parameter from above)
    elif current_gyro_reading > degrees:
        tank_block.on(left_speed = speed, right_speed = -speed)#turn the robot
        while current_gyro_reading > degrees:
            #print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)                
            current_gyro_reading = gyro.angle
            #gyro reading is smaller than target (once reached the degrees) stop program
            if current_gyro_reading <= degrees:
                break
            if stop():
                break
    tank_block.off()
    print("Leaving Turn_from_start_position", file=stderr)        
    print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)

