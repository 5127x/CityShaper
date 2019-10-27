# Demo of a simple proportional line follower using two sensors
# It's deliberately flawed and will exit with errors in some circumstances;
# try fixing it!

from ev3dev2.motor import  LargeMotor, MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep
from sys import stderr
#_______________________________________________________________________________
def FollowBlackLine_rotations(rotations, speed, colourSensor, lineSide, stop):
    
    colourLeft = ColorSensor(INPUT_3)
    colourRight = ColorSensor(INPUT_2)
    steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
    largeMotor_Left = LargeMotor(OUTPUT_B)
    largeMotor_Right = LargeMotor(OUTPUT_C)
    rotations = rotations * 360
    current_rotations = largeMotor_Left.position

    number = 0
    Average = 0
    total_RLI = 0

    target_rotations = float(rotations) + float(current_rotations)
    
    if colourSensor == "RIGHT":
        target_RLI = 50

            
    if colourSensor == "LEFT":
        target_RLI = 40

    while float(target_rotations) >= float(current_rotations):


        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity
            currentLeft_RLI = colourLeft.reflected_light_intensity
     
        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
            currentRightRLI = colourRight.reflected_light_intensity

    
        error = (float(target_RLI) - float(current_RLI))
        correction = error* 1.1

        if lineSide == "LEFT":
            correction = correction*-1
            if current_RLI >= 65:
                correction = error*-1.25
                #print("HEERE", file = stderr)


        if lineSide == "RIGHT":
            if current_RLI <= 10:
                correction = error*1.7

        if correction >= 100 :
            correction = 100
        if correction <= -100:
            correction = -100


        steering_drive.on(steering = correction, speed = speed)

        print(current_RLI, file = stderr)
        current_rotations = largeMotor_Left.position

    steering_drive.off()
#_______________________________________________________________________________

print ("Monkeys have tails")