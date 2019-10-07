block = False# Demo of a simple proportional line follower using two sensors
# It's deliberately flawed and will exit with errors in some circumstances;
# try fixing it!

from ev3dev2.motor import  LargeMotor, MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep

#_______________________________________________________________________________
def Looking4Black_Line_Follow(rotations, speed, colourSensor):

    colourLeft = ColorSensor(INPUT_2)
    colourRight = ColorSensor(INPUT_3)
    steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C) 
    largeMotor_Left = LargeMotor(OUTPUT_B)
    largeMotor_Right = LargeMotor(OUTPUT_C)
    target_RLI = 165
    prev_RLI = 300
    
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
    while current_RLI > 10:
        steering_drive.on(steering = 0, speed=speed)
        print("Looking for Black Line")
        if stop():
            break

        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
    #===========================================================================

    steering_drive.on_for_rotations(steering=0, speed=-speed, rotations = 0.01)
    print("GOING BACK")
    steering_drive.on(steering=0, speed=speed) 
    largeMotor_Left.on_for_rotations(rotations = .09, speed= -5)
    print("turns")

    #...................................................................................................
    #...................................................................................................
    #...................................................................................................
    
    while int(target_rotations) >= int(current_rotations):
        
        #print ("{} rotations left.".format (target_rotations/360 - current_rotations/360))
        
        if stop():
            break

        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity
            #print("Current COLOUR SENSOR RIGHT")

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
        #______________________________________________________________________________

        error = target_RLI - current_RLI
        if error >= 100:
            error == 99
            print("NEW ERROR{}".format (error))
            print("Changed ERROR")
        
        else:
            correction = error *1.01
            
        print("Correction: {} Error: {}".format (correction,error))
        
        steering_drive.on(steering=-correction, speed=speed*.9)


    
        # Do this after we have moved.  If we haven't reached the target_rotations, it will repeat again.
        current_rotations = largeMotor_Left.position

    steering_drive.off()
    print("NUMBER OF ROTATIONS HAS FINISHED")

# function(rotations = 4, speed = 14, colourSensor = "RIGHT" )
