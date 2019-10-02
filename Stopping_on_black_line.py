
from ev3dev2.motor import  LargeMotor, MoveSteering, MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep

colourLeft = ColorSensor(INPUT_2)
colourRight = ColorSensor(INPUT_3)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C) 
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)
largeMotor_Left = LargeMotor(OUTPUT_B)
largeMotor_Right = LargeMotor(OUTPUT_C)
target_RLI = 0
prev_RLI = 0
    

#_______________________________________________________________________________
def function(numberOfRotations, speed, LineSide, colourSensor):


    prev_RLI = 0
    numberOfRotations = numberOfRotations * largeMotor_Left.count_per_rot

    current_rotations = largeMotor_Left.position
    
    currentRight_RLI = colourRight.reflected_light_intensity
    currentLeft_RLI = colourLeft.reflected_light_intensity
    
    
    if colourSensor == "RIGHT":
        target_RLI = colourRight.reflected_light_intensity
        print("COLOUR SENSOR RIGHT")

    if colourSensor == "LEFT":
        target_RLI = colourLeft.reflected_light_intensity
        print ("COLOUR SENSOR LEFT")
        
        #_______________________________________________________________________
    stopping_rotations = float(numberOfRotations/360/1.9)
    print(stopping_rotations)
        #_______________________________________________________________________    
        

    target_rotations = int(numberOfRotations) + int(current_rotations)
  
    if colourSensor == "RIGHT":
        current_RLI = colourRight.reflected_light_intensity
            
    while current_RLI > 20:
        steering_drive.on(steering = 0, speed=speed)
        
        if colourSensor == "RIGHT":
            current_RLI = colourRight.reflected_light_intensity
            currentLeft_RLI = colourLeft.reflected_light_intensity

        if colourSensor == "LEFT":
            current_RLI = colourLeft.reflected_light_intensity
            currentRight_RLI = colourRight.reflected_light_intensity
    #===========================================================================
    print("FOUND BLACK LINE")
    steering_drive.on_for_rotations(steering=0, speed=-speed, rotations = 0.06)
    print("Reversing")
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
            print("Current RLI: {} Right RLI: {}  Prev RLI {}".format (current_RLI, currentRight_RLI, prev_RLI))
            print("Current Rotations{}".format (current_rotations/360))
            
            #________________________________________________________PRINTING
            

            if current_RLI <= 19:
                steering_drive.on(steering=-80, speed=speed)
                if int(current_rotations/360) >= stopping_rotations:
                    if prev_RLI == currentRight_RLI:
                            print("STOP")
                            steering_drive.off()
                            break

                        
            elif current_RLI > target_RLI:
                #print("right")
                steering_drive.on(steering=40, speed=speed)
                    
                if int(current_rotations/360) >= stopping_rotations:
                    if prev_RLI == currentRight_RLI:
                            print("STOP")
                            steering_drive.off()
                            break
                    
                        
            elif current_RLI < target_RLI:
                steering_drive.on(steering=-40, speed=speed) 

                if int(current_rotations/360) >= stopping_rotations:
                    if prev_RLI == currentRight_RLI:
                            print("STOP")
                            steering_drive.off()
                            break
                    
                
            else:
                #print ("Driving Foward")                
                steering_drive.on(steering=0, speed=speed)
    
                if int(current_rotations/360) >= stopping_rotations:
                    if prev_RLI == currentRight_RLI:
                            print("STOP")
                            steering_drive.off()
                            break
                    

        #__________________________
        #__________________________________________________________________________
        if LineSide == "RIGHT":
            print("Current RLI: {}  Target RLI: {}".format (current_RLI, target_RLI))
            #print ("Line side = Right") more  black
            if current_RLI < target_RLI:
                print("turn right")
                #print("")                
                steering_drive.on(steering=55, speed=speed)
                
            elif current_RLI > target_RLI:
                steering_drive.on(steering=-55, speed=speed) 
                print("turn left")
                #print("")less black                
                
            else:
                print ("Driving Foward")
                steering_drive.on(steering=0, speed=speed) 
        #__________________________________________________________________________

        if LineSide == "RIGHT":
            prev_RLI = colourLeft.reflected_light_intensity
            
        if LineSide == "LEFT":
            prev_RLI = colourRight.reflected_light_intensity
            
        current_rotations = largeMotor_Left.position
        #__________________________________________________________________________
    steering_drive.off()
    
    currentRight_RLI = colourRight.reflected_light_intensity
    currentLeft_RLI = colourLeft.reflected_light_intensity
        
    print ("")
    print ("")
    print ("")
    



function(numberOfRotations = 3, speed = 12, LineSide = "LEFT", colourSensor = "RIGHT" )
