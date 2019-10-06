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
    prev_RLI = 300
    
    numberOfRotations = numberOfRotations * largeMotor_Left.count_per_rot

    current_rotations = largeMotor_Left.position

    if colourSensor == "RIGHT":
        target_RLI = colourRight.reflected_light_intensity
        current_RLI = colourRight.reflected_light_intensity
        print("Previous COLOUR SENSOR RIGHT")

    if colourSensor == "LEFT":
        target_RLI = colourLeft.reflected_light_intensity
        current_RLI = colourLeft.reflected_light_intensity
        print ("Previous COLOUR SENSOR LEFT")
    

    target_rotations = int(numberOfRotations) + int(current_rotations)

    #...................................................................................................
    while current_RLI > 120:
        steering_drive.on(steering = 0, speed=speed)
        print("Looking for Black Line")
        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
    #===========================================================================

    steering_drive.on_for_rotations(steering=0, speed=-speed, rotations = 0.01)
    print("GOING BACK")
    steering_drive.on(steering=0, speed=speed) 
    largeMotor_Left.on_for_rotations(rotations = .07, speed= -5)
    print("turns")

    #...................................................................................................
    prev_RLI = current_RLI
    #...................................................................................................
    
    while int(target_rotations) >= int(current_rotations):
        
        #print ("{} rotations left.".format (target_rotations/360 - current_rotations/360))
        
        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity
            currentLeft_RLI = colourLeft.reflected_light_intensity            
            
        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
            currentRight_RLI  = colourRight.reflected_light_intensity


        #______________________________________________________________________________

        error = target_RLI - current_RLI
        if error >= 100:
            error == 99
            print("Changed ERROR")

            
        correction = error *1
        print("Correction: {} Error: {}".format (correction,error))
        
        steering_drive.on(steering=-correction, speed=speed)


        if prev_RLI >= 120:
            if currentLeft_RLI <= 30:
                print("FOUND BLACK")
                break
            else:
                continue
        
        # Do this after we have moved.  If we haven't reached the target_rotations, it will repeat again.
        current_rotations = largeMotor_Left.position
        prev_RLI = currentLeft_RLI
        
    steering_drive.off()
    

function(numberOfRotations = 2, speed = 13, colourSensor = "RIGHT" )
