block = False# Demo of a simple proportional line follower using two sensors
# It's deliberately flawed and will exit with errors in some circumstances;
# try fixing it!

from ev3dev2.motor import  LargeMotor, MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep

#_______________________________________________________________________________
def FollowBlackLine_rotations(stop, rotations, speed, colourSensor):

    colourLeft = ColorSensor(INPUT_2)
    colourRight = ColorSensor(INPUT_3)
    steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C) 
    largeMotor_Left = LargeMotor(OUTPUT_B)
    largeMotor_Right = LargeMotor(OUTPUT_C)
    target_RLI = 0
    
    rotations = rotations * 360

    current_degrees = largeMotor_Left.position

    if colourSensor == "RIGHT":
        target_RLI = colourRight.reflected_light_intensity
        print("Previous COLOUR SENSOR RIGHT")

    if colourSensor == "LEFT":
        target_RLI = colourLeft.reflected_light_intensity
        print ("Previous COLOUR SENSOR LEFT")


    target_rotations = int(rotations) + int(current_degrees)
  
    
    print ("Target Rotations ")
    print (target_rotations)
    print("")
    print ("Current Rotations ")
    print (current_degrees)
    correction = 0
    while int(target_rotations) >= int(current_degrees):
        
        #print ("{} rotations left.".format (target_rotations/360 - current_degrees/360))
        
        if stop():
            break

        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity
            #print("Current COLOUR SENSOR RIGHT")

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
        #______________________________________________________________________________

        error = target_RLI - current_RLI
        correction = error *1.01
        print("Correction: {} Error: {}".format (correction,error))
        steering_drive.on(steering=-correction, speed=speed)


    
        # Do this after we have moved.  If we haven't reached the target_rotations, it will repeat again.
        current_degrees = largeMotor_Left.position

    steering_drive.off()


# function(rotations = 2, speed = 15, colourSensor = "RIGHT" )
