
from ev3dev2.motor import MoveSteering, MoveTank, LargeMotor, OUTPUT_B, OUTPUT_C
#from ev3dev2.sensor.lego import ColorSensor, GyroSensor #TouchSensor,
from ev3dev2.sensor import  INPUT_2, INPUT_3
#import xml.etree.ElementTree as ET
#import threading
import time
#from sys import stderr

#colourLeft = ColorSensor(INPUT_3) # bcs apparently they have to be backwards...
#colourRight = ColorSensor(INPUT_2)
#gyro = GyroSensor(INPUT_1)

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
# mediumMotor_Left = MediumMotor(OUTPUT_A)
# mediumMotor = MediumMotor(OUTPUT_D)

def curving(stop, left_speed, right_speed, rotations): 
    target_rotations = rotations
    current_rotations = largeMotor_Left.position
    tank_block.on_for_rotations(right_speed=right_speed, left_speed=left_speed, rotations = rotations)
    
    '''
    while float(current_rotations) < target_rotations:
        print(target_rotations)
        tank_block.on_for_rotations(right_speed=right_speed, left_speed=left_speed)#, rotations = 0.1, brake = False)
        current_rotations = largeMotor_Left.position
        print("current rotations {}".format (current_rotations/360))
    '''
        
        
    tank_block.off()

curving(stop = False, left_speed = 20, right_speed = 15, rotations = 3)

        