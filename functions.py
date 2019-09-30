#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time

colourAttachment = ColorSensor(INPUT_4)
colourLeft = ColorSensor(INPUT_2)
colourRight = ColorSensor(INPUT_3)
gyro = GyroSensor(INPUT_1)

largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
mediumMotor_Left = MediumMotor(OUTPUT_A)
mediumMotor_Right = MediumMotor(OUTPUT_D)

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

prev_RLI = 0
#__________________________________________________________________Turning Certain amt or degrees   
def Turn_degrees(stop, speed, degrees):#gyro.mode=‘GYRO-ANG’    gyro.reset
    current_gyro_reading = gyro.angle
    print(“Current Gyro Reading: {}“.format(current_gyro_reading))
    
    if degrees < 0:
        while current_gyro_reading > degrees:
            print(“Turning LEFT”)
            current_gyro_reading = gyro.angle
            print(“Current Gyro Reading: {}“.format(current_gyro_reading))
            tank_block.on(right_speed = speed, left_speed = -speed)
            if stop():
                break

    if degrees > 0:
        while current_gyro_reading < degrees:
            print(“Turning RIGHT”)
            current_gyro_reading = gyro.angle
            print(“Current Gyro Reading: {}“.format(current_gyro_reading))
            tank_block.on(right_speed = -speed, left_speed = speed)
            if stop(): 
                break
    tank_block.off()
#_______________________________________________________________________________
def Straight_Gyro(stop, speed, rotations):
    current_degrees = largeMotor_Left.position # convert to degrees
    rotations = rotations * 360
    target_rotations = current_degrees+ rotations
    current_gyro_reading = gyro.angle
    print(“Current Gyro Reading: {}“.format(current_gyro_reading))

    while float(current_degrees) <  target_rotations:
        current_gyro_reading = gyro.angle

        if current_gyro_reading < 0:
            correction = 0 - current_gyro_reading
            correction = correction * .25
            print(“Turning Right”)
            print(“Current Gyro Reading: {}“.format(current_gyro_reading))
            steering_drive.on(steering = correction , speed = speed)

        if current_gyro_reading > 0:
            correction = 0 - current_gyro_reading
            correction = correction * .25   
            print(“Turning Left”)         
            print(“Current Gyro Reading: {}“.format(current_gyro_reading))
            steering_drive.on(steering = correction , speed = speed)

        if current_gyro_reading == 0:
            steering_drive.on(steering = 0 , speed = speed)
        if stop():
            break
    tank_block.off()
#_______________________________________________________________________________
def function(stop, rotations, speed, LineSide, colourSensor):
    prev_RLI = 0
    numberOfRotations =rotations* largeMotor_Left.count_per_rot
    current_rotations = largeMotor_Left.position

    if colourSensor == “RIGHT”:
        prev_RLI = colourRight.reflected_light_intensity
        print(“Previous COLOUR SENSOR RIGHT”)

    if colourSensor == “LEFT”:
        prev_RLI = colourLeft.reflected_light_intensity
        print (“Previous COLOUR SENSOR LEFT”)

    target_rotations = int(numberOfRotations) + int(current_rotations)
    print (“Target Rotations “)
    print (target_rotations)
    print(“”)
    print (“Current Rotations “)
    print (current_rotations)
    
    while int(target_rotations) = int(current_rotations):
        correction = 0.95
        if colourSensor == “RIGHT”:
            current_RLI = colourRight.reflected_light_intensity

        if colourSensor == “LEFT”:
            current_RLI = colourLeft.reflected_light_intensity

        if LineSide == “LEFT”:
            if current_RLI > prev_RLI:
                print(“turn right”)
                steering_drive.on(steering=50, speed=speed)
            elif current_RLI < prev_RLI:
                steering_drive.on(steering=-50, speed=speed) 
                print(“turn left”)
            else:
                print (“In loop line Left”)
                steering_drive.on(steering=0, speed=speed) 
        if LineSide == “RIGHT”:
            if current_RLI < prev_RLI:
                print(“turn right”)
                steering_drive.on(steering=50, speed=speed)
            elif current_RLI > prev_RLI:
                steering_drive.on(steering=-50, speed=speed) 
                print(“turn left”)
            else:
                steering_drive.on(steering=0, speed=speed) 

        current_rotations = largeMotor_Left.position
    steering_drive.off()
# function(numberOfRotations = 10, speed = 10, LineSide = “LEFT”, colourSensor = “RIGHT” )
#_______________________________________________________________________________
'''
def MediumMotor(stop, motor, numberOfRotations, speed): # do we really need this? we can just use onForRotations
    
    if motor == “Left”:
        motor = mediumMotor_Left
        mediumMotor_Left.on_for_rotations(rotations = numberOfRotations, speed = speed)
        
    if motor == “Right”:
        motor = mediumMotor_Right
        mediumMotor_Right.on_for_rotations(rotations = numberOfRotations, speed = speed)
#_______________________________________________________________________________
'''
#_______________________________________________________________________________

def squareOnLine(speed, threshold):
    colourLeft_RLI = 0
    colourRight_RLI = 0
    lineFound = False
    steering_drive.on(steering=0,speed=speed)
    while True:
        colourLeft_RLI = colourLeft.reflected_light_intensity
        colourRight_RLI = colourRight.reflected_light_intensity
        
        if colourLeft_RLI <= threshold:
            largeMotor_Left.on(-speed)
            largeMotor_Right.on(speed)
            lineFound = True
            print('{} left found it'.format(colourLeft_RLI))

        if colourRight_RLI <=threshold:
            largeMotor_Left.on(speed)
            largeMotor_Right.on(-speed)
            print('{} right found it'.format(colourRight_RLI))
        print('{} left, {} right'.format(colourLeft_RLI, colourRight_RLI))
    
        if colourLeft_RLI == colourRight_RLI and lineFound:
            break

#_______________________________________________________________________________
def onForRotations(stop, motor, speed, rotations, brake): 
    current_degrees = motor.position # there isnt a way to read rotations
    target_rotations = rotations * 360 # convert to degrees bcs its simpler
    target_rotations = current_degrees + target_rotations

    motor.on(speed=speed, brake=brake, block = False)
    while current_degrees < target_rotations:
        current_degrees = motor.position
        if stop():
            break
    motor.off()
#_______________________________________________________________________________ 
def Steering_rotations(stop, speed, rotations, steering, brake):
    current_degrees = motor.position # there isnt a way to read rotations
    target_rotations = rotations * 360 # convert to degrees bcs its simpler
    target_rotations = current_degrees + target_rotations
    steering_drive.on(steering = steering, speed= speed, brake = brake, block = False)
    while current_degrees < target_rotations:
        current_degrees = motor.position
        if stop():
            break
    steering_drive.off()
#_______________________________________________________________________________
def Steering_seconds(stop, speed, seconds, steering, brake): 
    start_time = time.time()
    steering_drive.on(speed, brake = brake, block = False)
    while time.time() < start_time + seconds:
        if stop():
            break
    steering_drive.off()
#_______________________________________________________________________________