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

#_______________________________________________________________________________
def LookingBlackLine_stopBlack(stop, rotations, speed, colourSensor):
    target_RLI = 165
    prev_RLI = 300
    error1 = 0
    
    rotations = rotations * largeMotor_Left.count_per_rot

    current_rotations = largeMotor_Left.position

    if colourSensor == "RIGHT":

        current_RLI = colourRight.reflected_light_intensity
        print("Previous COLOUR SENSOR RIGHT")

    if colourSensor == "LEFT":
        current_RLI = colourLeft.reflected_light_intensity
        print ("Previous COLOUR SENSOR LEFT")
    

    target_rotations = int(rotations) + int(current_rotations)

    #...................................................................................................
    while current_RLI >= 12:
        steering_drive.on(steering = 0, speed=speed)
        print(current_RLI)
        if stop():
            break
        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
    #=========================================================================== # maybe change to function? ? ?
    
    steering_drive.on_for_rotations(steering=0, speed=-speed, rotations = 0.01)
    print("GOING BACK")
    steering_drive.on(steering=0, speed=speed) 
    largeMotor_Left.on_for_rotations(rotations = .09, speed= -5)
    print("turns")

    #...................................................................................................
    #...................................................................................................
    #...................................................................................................
    
    while int(target_rotations) >= float(current_rotations):
        
        #print ("{} rotations left.".format (target_rotations/360 - current_rotations/360))
        if stop():
            break

        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity
            currentLeft_RLI = colourLeft.reflected_light_intensity
            prevOpposite_RLI = colourLeft.reflected_light_intensity

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
            currentRightRLI = colourRight.reflected_light_intensity
            prevOpposite_RLI = colourRight.reflected_light_intensity
        #______________________________________________________________________________
        error = target_RLI - current_RLI
        print("Error: {}".format (error))
        if int(error) > 99:
            error = 99
            
            print("NEW ERROR {}".format (error))

        
        
        correction = error *1.01
            
        
        steering_drive.on(steering=-correction, speed=speed*.9)
        
        if colourSensor == "RIGHT":
            if currentLeft_RLI <= 20:
                print("FOUND BLACK LINE")
                break
                
                print("PREV {} current L {}".format (prevOpposite_RLI,currentLeft_RLI))
                prevOpposite_RLI = currentLeft_RLI
        
        if colourSensor == "LEFT":
            if currentRight_RLI <= 20:
                print("FOUND BLACK LINE")
                break
                
                print("PREV {} current R {}".format (prevOpposite_RLI,currentRight_RLI))
                prevOpposite_RLI = currentRight_RLI
        current_rotations = largeMotor_Left.position
    
    steering_drive.off()
    

# LookingBlackLine_stopBlack(rotations = 4, speed = 14, colourSensor = "RIGHT" )
