# Demo of a simple proportional line follower using two sensors
# It's deliberately flawed and will exit with errors in some circumstances;
# try fixing it!

from ev3dev2.motor import  LargeMotor, MoveSteering, MediumMotor, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep

colourLeft = ColorSensor(INPUT_2)
colourRight = ColorSensor(INPUT_3)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C) 
largeMotor_Left = LargeMotor(OUTPUT_B)
largeMotor_Right = LargeMotor(OUTPUT_C)
#mediumMotor_Left = MediumMOtor(OUTPUT_A)
mediumMotor = MediumMOtor(OUTPUT_D)

    

#_______________________________________________________________________________
def MediumMotor(whichMotor,numberOfRotations, speed):
    #===========================================================================
    '''if whichMotor = "Left":
        whichMotor = mediumMotor_Left
        mediumMotor_Left.on_for_rotations(rotations = numberOfRotations, speed = speed)'''
    #===========================================================================    
    if whichMotor = "Right":
        whichMotor = mediumMotor_Right
        mediumMotor_Right.on_for_rotations(rotations = numberOfRotations, speed = speed)
    #===========================================================================