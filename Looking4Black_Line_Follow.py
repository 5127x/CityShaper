# Demo of a simple proportional line follower using two sensors
# It's deliberately flawed and will exit with errors in some circumstances;
# try fixing it!

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
    while int(target_rotations ) >= int(current_rotations):
        
        correction = 0.95
        
        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity


        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity

        #======================================================================
        
        
       #__________________________________________________________________________
        
        #print ("In loop line 65")
        if LineSide == "LEFT":
            print(current_RLI, prev_RLI)
        
            if current_RLI - prev_RLI > 1:
                
                if current_RLI > prev_RLI:
                    print("turn right")
                    
                    #More Black
                    steering_drive.on(steering=80, speed=speed)
                    
                elif current_RLI < prev_RLI:
                    steering_drive.on(steering=-80, speed=speed) 
                    print("turn left")
                    #Less Black
                    
                    
                else:
                    print ("DRIVING FOWARD")                
                    steering_drive.on(steering=0, speed=speed) 
                    
            elif current_RLI+prev_RLI == 510:
                print("LARGE TURN RIGHT")
                largeMotor_Right.on_for_rotations(rotations = .00002, speed= -5, brake = False)
                
            else:
                print ("DRIVING FOWARD ______ 1")                
                steering_drive.on(steering=0, speed=speed) 
        #__________________________________________________________________________
        if LineSide == "RIGHT":
            #print ("Line side = Right") more  black
            if current_RLI < prev_RLI:
                print("turn right")
                #Less Black                
                steering_drive.on(steering=-80, speed=speed)
                
            elif current_RLI > prev_RLI:
                steering_drive.on(steering=80, speed=speed) 
                print("turn left")
                #More White            
                
            else:
                print ("DRIVING FOWARD") 
                steering_drive.on(steering=0, speed=speed) 
        #__________________________________________________________________________

    

        current_rotations = largeMotor_Left.position
        prev_RLI = current_RLI

    steering_drive.off()
 #_______________________________________________________________________________Taking Input


#numberOfRotations, speed, LineSide, colourSensor):

function(numberOfRotations = 10, speed = 7, LineSide = "LEFT", colourSensor = "RIGHT" )
#_______________________________________________________________________________

#LEFT RIGHT _______ 1041 125  f
#LEFT LEFT ________ 1080 125  t
#RIGHT RIGHT________ 1067 125 t until 1/2 way between 2nd and third corner  t
#Right LEft__________ 1110 125 t until third corner and comes back the other way t
