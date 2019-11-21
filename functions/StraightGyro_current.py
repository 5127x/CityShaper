
#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

gyro = GyroSensor(INPUT_1)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)

#_________________________________________________________________________________________________________________________________
def StraightGyro_current(stop, speed, rotations):
    print("In StraightGyro_current", file=stderr)
    current_degrees = largeMotor_Left.position 
    rotations = rotations * 360
    target_rotations= current_degrees + rotations
    target = gyro.angle
    current_gyro_reading = target
    # print("Current Gyro Reading: {}".format(current_gyro_reading))

    while float(current_degrees) < target_rotations: # if the currentm rotations is smaller than the target rotations
        if stop(): 
            break
        #recording the gyro reading  and the current rotations
        current_gyro_reading=gyro.angle
        current_degrees = largeMotor_Left.position

        # if the gyro reading is smaller than the target (Going to the right)
        if current_gyro_reading < target:
            correction = target - current_gyro_reading #figure out correction by target gyro reading - the current reading
            correction = correction * .25 # find a 1/4 of the correction 
            steering_drive.on(steering = -correction , speed = speed) #turns by the corrrection

        # if the gyro reading is larger than the target (Going to the left)
        if current_gyro_reading > target:
            correction = target - current_gyro_reading#figure out correction by target gyro reading - the current reading
            correction = correction * .25 # find a 1/4 of the correction 
            steering_drive.on(steering = -correction , speed = speed) #turns by the corrrection

        # if the current gyro = the target just continue straight
        if current_gyro_reading == target:
            steering_drive.on(steering = 0 , speed = speed)

        #if the current rotations is larger than the target break which will stop the loop
        if float(current_degrees) >= target_rotations:
            break
        if stop():
            break
    tank_block.off()
    print('Leaving StraightGyro_current', file=stderr)

#stopProcessing=False
#StraightGyro_current(lambda:stopProcessing, speed=30, rotations=3)
