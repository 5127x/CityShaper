#This one is combined with the wirerd one wihout the wierd tur LARGE RIGHT

# Demo of a simple proportional line follower using two sensors
# It's deliberately flawed and will exit with errors in some circumstances;
# try fixing it!
#ev3.dev2
from ev3dev2.motor import  LargeMotor, MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep

colourLeft = ColorSensor(INPUT_2)
colourRight = ColorSensor(INPUT_3)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C) 
largeMotor_Left = LargeMotor(OUTPUT_B)
largeMotor_Right = LargeMotor(OUTPUT_C)
prev_RLI = 0
    

#_______________________________________________________________________________
def function(numberOfRotations, speed, LineSide, colourSensor):


    
    numberOfRotations = numberOfRotations * largeMotor_Left.count_per_rot

    current_rotations = largeMotor_Left.position

    if colourSensor == "RIGHT":
        prev_RLI = colourRight.reflected_light_intensity
        print("COLOUR SENSOR RIGHT")

    if colourSensor == "LEFT":
        prev_RLI = colourLeft.reflected_light_intensity
        print ("COLOUR SENSOR LEFT")
        
        #_______________________________________________________________________
     
        #_______________________________________________________________________    
        

    target_rotations = int(numberOfRotations) + int(current_rotations)
  
    if colourSensor == "RIGHT":
        current_RLI = colourRight.reflected_light_intensity
            
    while current_RLI > 10:
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
    #===========================================================================
    while int(target_rotations) >= int(current_rotations):
        
        correction = 0.95
        
        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity
            #print("Current COLOUR SENSOR RIGHT")

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
            #print ("Current COLOUR SENSOR LEFT")

        
    
        #print ("Current Rotations: ",(current_rotations))
        #print("Current Light Reading: ", current_RLI, "Previous Light Reading: ", prev_RLI)
        
        # with a steering_drive, we can slow the left or right wheel down to get the robot to turn that way.
        #steering_drive.on_for_rotations(steering=0, speed=50, rotations = 2

       #__________________________________________________________________________
        
        #print ("In loop line 65")
        if LineSide == "LEFT":
            #print ("Line side = Left")
            if current_RLI > prev_RLI:
                print("turn right")
                #print("")
                steering_drive.on(steering=55, speed=speed)
                
            elif current_RLI < prev_RLI:
                steering_drive.on(steering=-55, speed=speed) 
                print("turn left")
              #  print("")
                
                
            else:
                print ("In loop line Left")                
                steering_drive.on(steering=0, speed=speed) 
        #__________________________________________________________________________
        if LineSide == "RIGHT":
            #print ("Line side = Right") more  black
            if current_RLI < prev_RLI:
                print("turn right")
                #print("")                
                steering_drive.on(steering=55, speed=speed)
                
            elif current_RLI > prev_RLI:
                steering_drive.on(steering=-55, speed=speed) 
                print("turn left")
                #print("")less black                
                
            else:
                #print ("In loop line Left")
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

        