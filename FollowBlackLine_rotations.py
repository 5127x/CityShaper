# Demo of a simple proportional line follower using two sensors
# It's deliberately flawed and will exit with errors in some circumstances;
# try fixing it!

from ev3dev2.motor import  LargeMotor, MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep
from sys import stderr
#_______________________________________________________________________________
def FollowBlackLine_rotations(rotations, speed):
    
    colorLeft = ColorSensor(INPUT_3)
    colorRight = ColorSensor(INPUT_2)
    steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
    largeMotor_Left = LargeMotor(OUTPUT_B)
    largeMotor_Right = LargeMotor(OUTPUT_C)
    rotations = rotations * 360
    current_rotations = largeMotor_Left.position
    target_RLI = 69

    target_rotations = float(rotations) + float(current_rotations)
    #print ("target rotations {}".format(target_rotations), file=stderr)
    while float(target_rotations) >= float(current_rotations):
        current_RLI = colorRight.reflected_light_intensity
        error = (float(target_RLI) - float(current_RLI))
        correction = error* .9
        if current_RLI >= 100:
            correction = error*1.4
        '''
        if correction > 100:
            correction = 100
        '''
        #print("correction = {}".format(correction), file=stderr)
        #print("current RLI = {}".format(current_RLI), file=stderr)

        steering_drive.on(steering = correction, speed = speed, brake = False)


        current_rotations = largeMotor_Left.position

    steering_drive.off()
#_______________________________________________________________________________

print ("Monkeys have tails")