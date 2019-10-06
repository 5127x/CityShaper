block = False# Demo of a simple proportional line follower using two sensors
# It's deliberately flawed and will exit with errors in some circumstances;
# try fixing it!

from ev3dev2.motor import  LargeMotor, MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep

#_______________________________________________________________________________
def function(numberOfRotations, speed, colourSensor):

    colourLeft = ColorSensor(INPUT_2)
    colourRight = ColorSensor(INPUT_3)
    steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C) 
    largeMotor_Left = LargeMotor(OUTPUT_B)
    largeMotor_Right = LargeMotor(OUTPUT_C)
    target_RLI = 0
    
    numberOfRotations = numberOfRotations * largeMotor_Left.count_per_rot

    current_rotations = largeMotor_Left.position

    if colourSensor == "RIGHT":
        target_RLI = colourRight.reflected_light_intensity
        print("Previous COLOUR SENSOR RIGHT")

    if colourSensor == "LEFT":
        target_RLI = colourLeft.reflected_light_intensity
        print ("Previous COLOUR SENSOR LEFT")


    target_rotations = int(numberOfRotations) + int(current_rotations)
  
    
    print ("Target Rotations ")
    print (target_rotations)
    print("")
    print ("Current Rotations ")
    print (current_rotations)
    correction = 0
    while int(target_rotations) >= int(current_rotations):
        
        
        
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
        current_rotations = largeMotor_Left.position

    steering_drive.off()


function(numberOfRotations = 10, speed = 10, colourSensor = "RIGHT" )
