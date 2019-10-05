block = False# Demo of a simple proportional line follower using two sensors
# It's deliberately flawed and will exit with errors in some circumstances;
# try fixing it!

from ev3dev2.motor import  LargeMotor, MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from time import sleep

#_______________________________________________________________________________
def function(numberOfRotations, speed, LineSide, colourSensor):

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
    
    while int(target_rotations) >= int(current_rotations):
        
        correction = 0.95
        
        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity
            #print("Current COLOUR SENSOR RIGHT")

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
        #______________________________________________________________________________
        if LineSide == "LEFT":
            error = target_RLI - current_RLI
            correction = error *.25
            steering_drive.on(steering=correction, speed=speed)

        #__________________________________________________________________________
        if LineSide == "RIGHT":
            #print ("Line side = Right") more  black
            if current_RLI < target_RLI:
                print("turn right")
                #print("")                
                steering_drive.on(steering=50, speed=speed)
                
            elif current_RLI > target_RLI:
                steering_drive.on(steering=-50, speed=speed) 
                print("turn left")
                #print("")less black                
                
            else:

                steering_drive.on(steering=0, speed=speed) 
        #__________________________________________________________________________

    
        # Do this after we have moved.  If we haven't reached the target_rotations, it will repeat again.
        current_rotations = largeMotor_Left.position
        #print ("Current Rotations2: ",(current_rotations))

    # We have gone the required distance, stop the motor.
    steering_drive.off()
 #_______________________________________________________________________________Taking Input

#_______________________________________________________________________________Defining Colour Sensor
#numberOfRotations, speed, LineSide, colourSensor):

function(numberOfRotations = 10, speed = 10, LineSide = "LEFT", colourSensor = "RIGHT" )
#_______________________________________________________________________________

#LEFT RIGHT _______ 1041 125  f
#LEFT LEFT ________ 1080 125  t
#RIGHT RIGHT________ 1067 125 t until 1/2 way between 2nd and third corner  t
#Right LEft__________ 1110 125 t until third corner and comes back the other way t

        