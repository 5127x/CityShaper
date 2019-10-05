
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
def Stopping_on_black_line(numberOfRotations, speed, LineSide, colourSensor):


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
    stopping_rotations = float(numberOfRotations/360/1.9584)
    print float(stopping_rotations)
        #_______________________________________________________________________    
        

    target_rotations = int(numberOfRotations) + int(current_rotations)
  
    if colourSensor == "RIGHT":
        current_RLI = colourRight.reflected_light_intensity
    
    steering_drive.on_for_rotations(steering=0, rotations=.25, speed=speed) 
    print("Searching")
    
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
           
            currentLeft_RLI = colourLeft.reflected_light_intensity
            #print("Current RLI: {}___Prev RLI {}___Left Colour {} ".format (current_RLI,  prev_RLI, currentLeft_RLI))
            #print("                                                 CR {}".format (current_rotations/360))
            
            #________________________________________________________PRINTING
            
            if (current_rotations/360) >= stopping_rotations:
                if prev_RLI >= 100:
                    if currentLeft_RLI <= 30:
                        print("STOP")
                        steering_drive.off()
                        break
                    
                    elif current_RLI <= 25:
                        steering_drive.on(steering=-50, speed=speed)
                        print("LARGE TURN")
                
                    else:
                        print("NO")
                        continue
            
            elif current_RLI <= 25:
                steering_drive.on(steering=-75, speed=speed)
                print("LARGE TURN")

            
            elif current_RLI > target_RLI:
                if currentLeft_RLI <= 100:
                    steering_drive.on(steering=40, speed=speed/1.5)
                else:
                    steering_drive.on(steering=40, speed=speed)

                    
                        
            elif current_RLI < target_RLI:
                if currentLeft_RLI <= 100:
                    steering_drive.on(steering=-40, speed=speed/1.5)
                else:
                    steering_drive.on(steering=-40, speed=speed)



                
            else:
                if currentLeft_RLI <= 100:
                    steering_drive.on(steering=0, speed=speed/1.5)
                else:
                    steering_drive.on(steering=0, speed=speed)

        #__________________________
        #__________________________________________________________________________
        if LineSide == "RIGHT":
            currentRight_RLI = colourRight.reflected_light_intensity
            #print("Current RLI: {} Current RIGHT RLI {}  Prev RLI {}".format (current_RLI,currentRight_RLI, prev_RLI))
            #print("Current Rotations{}".format (current_rotations/360))
            
            #________________________________________________________PRINTING
            

            if int(current_rotations/360) >= stopping_rotations:
                    if prev_RLI == currentRight_RLI:
                            print("STOP")
                            steering_drive.off()
                            break
            
            elif current_RLI <= 19:
                steering_drive.on(steering=80, speed=speed)
                

            
            elif current_RLI > target_RLI:
                #print("right")
                steering_drive.on(steering=-40, speed=speed)

                    
                        
            elif current_RLI < target_RLI:
                steering_drive.on(steering=40, speed=speed) 


                
            else:
                #print ("Driving Foward")                
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
    currentLeft_RLI = cdolourLeft.reflected_light_intensity
        
    print ("")
    print ("")
    print ("")
    



Stopping_On_Black_Line(numberOfRotations = 3, speed = 15, LineSide = "LEFT", colourSensor = "RIGHT" )
