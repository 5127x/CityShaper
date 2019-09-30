# Demo of a simple proportional line follower using two sensors
# It's deliberately flawed and will exit with errors in some circumstances;
# try fixing it!

from ev3dev2.motor import  LargeMotor, MoveSteering, MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep

colourLeft = ColorSensor(INPUT_2)
colourRight = ColorSensor(INPUT_3)
gyro = GyroSensor(INPUT_4)
largeMotor_Left = LargeMotor(OUTPUT_B)
largeMotor_Right = LargeMotor(OUTPUT_C)
prev_RLI = 0
#_______________________________________________________________________________
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

    
def Turn_degrees(speed, degrees):
    
   # gyro.mode='GYRO-ANG'
    #gyro.reset
    current_gyro_reading = gyro.angle
    print("Current Gyro Reading: {}".format(current_gyro_reading))
    
 #===========================================================================
 #===========================================================================
    if degrees < 0:
        while current_gyro_reading > degrees:
            print("Turning LEFT")
            current_gyro_reading = gyro.angle
            print("Current Gyro Reading: {}".format(current_gyro_reading))
            tank_block.on(right_speed = speed, left_speed = -speed)
            
    #===========================================================================
    
    if degrees > 0:
        while current_gyro_reading < degrees:
            print("Turning RIGHT")
            current_gyro_reading = gyro.angle
            print("Current Gyro Reading: {}".format(current_gyro_reading))
            tank_block.on(right_speed = -speed, left_speed = speed)
            
    
    tank_block.off()
Turn_degrees(20, -180)

    
