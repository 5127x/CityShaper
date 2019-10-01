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
Target_RLI = 0
prev_RLI = 0
RLFL360 = 0
#_______________________________________________________________________________
def function(numberOfRotations, Rotations_looking_for_line, speed, LineSide, colourSensor):


    
    numberOfRotations = numberOfRotations * largeMotor_Left.count_per_rot

    current_rotations = largeMotor_Left.position

    if colourSensor == "RIGHT":
        Target_RLI = colourRight.reflected_light_intensity
        prev_RLI = colourRight.reflected_light_intensity

        print("COLOUR SENSOR RIGHT")

    if colourSensor == "LEFT":
        Target_RLI = colourLeft.reflected_light_intensity
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
            currentLeft_RLI = colourLeft.reflected_light_intensity

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
            currentRight_RLI = colourRight.reflected_light_intensity
    #===========================================================================

    steering_drive.on_for_rotations(steering=0, speed=-speed, rotations = 0.01)
    print("GOING BACK")
    steering_drive.on(steering=0, speed=speed) 
    largeMotor_Left.on_for_rotations(rotations = .07, speed= -5)
    print("turns")
    #===========================================================================
    while int(target_rotations) >= float(current_rotations):
        
        RLFL360 == int(Rotations_looking_for_line)*360
        print(RLFL360)
        
        print("Current Rotations {}".format (current_rotations/360))
        
        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity
            currentLeft_RLI = colourLeft.reflected_light_intensity
            #prev_RLI = colourRight.reflected_light_intensity

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
            currentRight_RLI = colourRight.reflected_light_intensity
            #prev_RLI = colourLeft.reflected_light_intensity

       #__________________________________________________________________________
        
        #print ("In loop line 65")
        if LineSide == "LEFT":
           
            currentRight_RLI = colourRight.reflected_light_intensity
            print("Current RLI: {}  Target: {}  Prev RLI: {}  Right: {}".format (current_RLI, Target_RLI, prev_RLI, currentRight_RLI))
            if current_RLI > Target_RLI:
                #print("right")
                steering_drive.on(steering=55, speed=speed)
                
                if target_rotations  >= RLFL360:
                    print("_________________________________________________")
                    if prev_RLI >= 110:
                        print("ON WHITE")
                        if currentRight_RLI <= 105:
                            print("STOP")
                            break
                    
            elif current_RLI < Target_RLI:
                steering_drive.on(steering=-55, speed=speed) 

                if target_rotations  >= RLFL360:
                    print("_________________________________________________")
                    if prev_RLI >= 110:
                        print("ON WHITE")
                        if currentRight_RLI <= 105:
                            print("STOP")
            
            else:
                #print ("Driving Foward")                
                steering_drive.on(steering=0, speed=speed)

                if target_rotations  >= RLFL360:
                    print("_________________________________________________")
                    if prev_RLI >= 110:
                        print("ON WHITE")
                        if currentRight_RLI <= 105:
                            print("STOP")
        #__________________________________________________________________________
        if LineSide == "RIGHT":
            print("Current RLI: {}  targt: {}".format (current_RLI, Target_RLI))
            #print ("Line side = Right") more  black
            if current_RLI < Target_RLI:
                print("turn right")
                #print("")                
                steering_drive.on(steering=55, speed=speed)
                
            elif current_RLI > Target_RLI:
                steering_drive.on(steering=-55, speed=speed) 
                print("turn left")
                #print("")less black                
                
            else:
                print ("Driving Foward")
                steering_drive.on(steering=0, speed=speed) 
        #__________________________________________________________________________

    
        # Do this after we have moved.  If we haven't reached the target_rotations, it will repeat again.
        current_rotations = largeMotor_Left.position
        if colourSensor == "RIGHT":
            prev_RLI = colourRight.reflected_light_intensity

        if colourSensor == "LEFT":
            prev_RLI = colourLeft.reflected_light_intensity
        #print ("Current Rotations2: ",(current_rotations))

    # We have gone the required distance, stop the motor.
    steering_drive.off()
 #_______________________________________________________________________________Taking Input

#_______________________________________________________________________________Defining Colour Sensor
#numberOfRotations, speed, LineSide, colourSensor):

function(numberOfRotations = 2,Rotations_looking_for_line = 1, speed = 12, LineSide = "LEFT", colourSensor = "RIGHT" )
#_______________________________________________________________________________

#LEFT RIGHT _______ 1041 125  f
#LEFT LEFT ________ 1080 125  t
#RIGHT RIGHT________ 1067 125 t until 1/2 way between 2nd and third corner  t
#Right LEft__________ 1110 125 t until third corner and comes back the other way t

        