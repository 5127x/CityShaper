#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

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

def BlackLine_colourStop(stop, speed, sensor, lineSide, correction):
    rotations = rotations*360
    currentDegrees_left = largeMotor_Left.position
    currentDegrees_right = largeMotor_Right.position
    target_left = currentDegrees_left + rotations
    target_right = currentDegrees_right + rotations
    right_RLI = colourRight.reflected_light_intensity
    left_RLI = colourLeft.reflected_light_intensity
    target_RLI = 40
    
    #if the colour sensor that you are using = Right then do this part of the program (being called from defined section above)
    if sensor == "RIGHT":
        #Choosing which side of the line to follow
        
        if lineSide == "LEFT":
            while left_RLI > 20: 
                #and currentDegrees_right < target_right:
                currentDegrees_left = largeMotor_Left.position
                #currentDegrees_right = largeMotor_Right.position
                right_RLI = colourRight.reflected_light_intensity
                left_RLI = colourLeft.reflected_light_intensity
                error = right_RLI - target_RLI

                steering = 0

                if abs(error) < 5: #If the absaloute error (positive error) is smaller than 5
                    steering = error * 0.25

                elif abs(error) >= 5 and abs(error) <=10: #If the absaloute error (positive error) is larger of equal to 5 AND smaller than 10
                    steering = error * 0.5

                elif abs(error) >= 10 and abs(error) <=25: #If the absaloute error (positive error) is larger of equal to 10 AND smaller or equal to 25
                    steering = error * 1 

                elif abs(error) >= 25:
                    steering = error * 1.25
                
                #steering = error * correction

                steering_drive.on(speed=speed, steering = steering)
                if stop():
                    break
        #Choosing which side of the line to follow
        elif lineSide == "RIGHT":
            while currentDegrees_left < target_left and currentDegrees_right < target_right:
                currentDegrees_left = largeMotor_Left.position
                currentDegrees_right = largeMotor_Right.position
                right_RLI = colourRight.reflected_light_intensity
                error = target_RLI - right_RLI
                steering = error * correction
                steering_drive.on(speed=speed, steering = steering)
                if stop():
                    break


    #if the colour sensor that you are using = Right then do this part of the program (being called from defined section above)                  

    elif sensor == "LEFT":

        #Choosing which side of the line to follow
        if lineSide == "RIGHT":
            
            while currentDegrees_left < target_left and currentDegrees_right < target_right:
                currentDegrees_left = largeMotor_Left.position
                currentDegrees_right = largeMotor_Right.position
                left_RLI = colourLeft.reflected_light_intensity
                error = target_RLI - right_RLI 
                steering = error * correction
                steering_drive.on(speed=speed, steering = steering)
                if stop():
                    break

        #Choosing which side of the line to follow
        elif lineSide == "LEFT":
            while currentDegrees_left < target_left and currentDegrees_right < target_right:
                currentDegrees_left = largeMotor_Left.position
                currentDegrees_right = largeMotor_Right.position
                left_RLI = colourLeft.reflected_light_intensity
                error = left_RLI - target_RLI 
                steering = error * correction
                steering_drive.on(speed=speed, steering = steering)
                if stop():
                    break
    steering_drive.off()
