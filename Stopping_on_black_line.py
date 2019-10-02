
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
    stopping_rotations = float(numberOfRotations/360/2)
    print(stopping_rotations)
        #_______________________________________________________________________    
        

    target_rotations = int(numberOfRotations) + int(current_rotations)
  
    if colourSensor == "RIGHT":
        current_RLI = colourRight.reflected_light_intensity
            
    while current_RLI > 20:
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
    while int(target_rotations) >= int(current_rotations):
        
        correction = 0.95
        
        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity
            currentLeft_RLI = colourLeft.reflected_light_intensity

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
            currentRight_RLI = colourRight.reflected_light_intensity

       #__________________________________________________________________________
        

        if LineSide == "LEFT":
           
            currentRight_RLI = colourRight.reflected_light_intensity
            print("Current RLI: {}  Previous RLI: {}  Right: {}".format (current_RLI, prev_RLI, currentRight_RLI))
            print("Current Rotations{}".format (current_rotations/360))
            
            #________________________________________________________PRINTING
            
            
            if current_RLI > prev_RLI:
                #print("right")
                steering_drive.on(steering=55, speed=speed)
                
                if int(current_rotations/360) >= stopping_rotations:
                    ("____________________________________________")
                    if currentRight_RLI <= 100:
                        print("STOP")
                        break
                    
            elif current_RLI < prev_RLI:
                steering_drive.on(steering=-55, speed=speed) 

                if int(current_rotations/360) >= stopping_rotations:
                    ("____________________________________________")
                    if currentRight_RLI <= 15:
                        print("STOP")
                        break
            
            else:
                print ("Driving Foward")                
                steering_drive.on(steering=0, speed=speed)

                if float(current_rotations/360) >= stopping_rotations:
                    ("____________________________________________")
                    if currentRight_RLI <= 15:
                        print("STOP")
                        break
        #__________________________________________________________________________
        if LineSide == "RIGHT":
            print("Current RLI: {}  Previous RLI: {}".format (current_RLI, prev_RLI))
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
                print ("Driving Foward")
                steering_drive.on(steering=0, speed=speed) 
        #__________________________________________________________________________

    
        current_rotations = largeMotor_Left.position

    steering_drive.off()
 #_______________________________________________________________________________Taking Input

#_______________________________________________________________________________Defining Colour Sensor
#numberOfRotations, speed, LineSide, colourSensor):

function(numberOfRotati
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
    stopping_rotations = float(numberOfRotations/360/2)
    print(stopping_rotations)
        #_______________________________________________________________________    
        

    target_rotations = int(numberOfRotations) + int(current_rotations)
  
    if colourSensor == "RIGHT":
        current_RLI = colourRight.reflected_light_intensity
            
    while current_RLI > 20:
        steering_drive.on(steering = 0, speed=speed)
        print("Looking")
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
    while int(target_rotations) >= int(current_rotations):

        
        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity
            currentLeft_RLI = colourLeft.reflected_light_intensity

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
            currentRight_RLI = colourRight.reflected_light_intensity

       #__________________________________________________________________________
        

        if LineSide == "LEFT":
           
            currentRight_RLI = colourRight.reflected_light_intensity
            print("Current RLI: {}  Previous RLI: {}  Right: {}".format (current_RLI, prev_RLI, currentRight_RLI))
            print("Current Rotations{}".format (current_rotations/360))
            
            #________________________________________________________PRINTING
            
            
            if current_RLI > prev_RLI:
                #print("right")
                steering_drive.on(steering=55, speed=speed)
                
                if int(current_rotations/360) >= stopping_rotations:
                    if currentRight_RLI <= 15:
                        print("STOP")
                        break
                    
            elif current_RLI < prev_RLI:
                steering_drive.on(steering=-55, speed=speed) 

                if int(current_rotations/360) >= stopping_rotations:

                    if currentRight_RLI <= 15:
                        print("STOP")
                        break
            
            else:
                print ("Driving Foward")                
                steering_drive.on(steering=0, speed=speed)

                if float(current_rotations/360) >= stopping_rotations:
                    
                    if currentRight_RLI <= 15:
                        print("STOP")
                        break
        #__________________________________________________________________________
        if LineSide == "RIGHT":
            print("Current RLI: {}  Previous RLI: {}".format (current_RLI, prev_RLI))
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
                print ("Driving Foward")
                steering_drive.on(steering=0, speed=speed) 
        #__________________________________________________________________________

    
        current_rotations = largeMotor_Left.position

    steering_drive.off()
 #_______________________________________________________________________________Taking Input

#_______________________________________________________________________________Defining Colour Sensor
#numberOfRotations, speed, LineSide, colourSensor):

function(numberOfRotations = 3, speed = 12, LineSide = "LEFT", colourSensor = "RIGHT" )
#_______________________________________________________________________________

#LEFT RIGHT _______ 1041 125  f
#LEFT LEFT ________ 1080 125  t
#RIGHT RIGHT________ 1067 125 t until 1/2 way between 2nd and third corner  t
#Right LEft__________ 1110 125 t until third corner and comes back the other way t

        ons = 3, speed = 12, LineSide = "LEFT", colourSensor = "RIGHT" )
#_______________________________________________________________________________

#LEFT RIGHT _______ 1041 125  f
#LEFT LEFT ________ 1080 125  t
#RIGHT RIGHT________ 1067 125 t until 1/2 way between 2nd and third corner  t
#Right LEft__________ 1110 125 t until third corner and comes back the other way t

        