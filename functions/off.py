from ev3dev2.motor import  MediumMotor, LargeMotor, MoveSteering, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep
from sys import stderr
colourLeft = ColorSensor(INPUT_3) 
colourRight = ColorSensor(INPUT_2)
gyro = GyroSensor(INPUT_1)

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
mediumMotor = MediumMotor(OUTPUT_D)
#_________________________________________________________________________________________________________________________________


def off ():
    # turn brake off on the motors
    print('Turning motors off', file=stderr)
    largeMotor_Left.off(brake = False)
    largeMotor_Right.off(brake = False)
    mediumMotor.off(brake = False)
