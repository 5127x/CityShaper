from ev3dev2.motor import MoveSteering, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor, INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time

colourAttachment = ColorSensor(INPUT_4)
colourLeft = ColorSensor(INPUT_2)
colourRight = ColorSensor(INPUT_3)
gyro = GyroSensor(INPUT_1)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
# mediumMotor_Left = MediumMotor(OUTPUT_A)
mediumMotor = MediumMotor(OUTPUT_D)

def squareOnLine(stop, speed, target):
    colourLeft_RLI = 0
    colourRight_RLI = 0
    lineFound = False
    steering_drive.on(steering=0,speed=speed)
    while True:
        colourLeft_RLI = colourLeft.reflected_light_intensity
        colourRight_RLI = colourRight.reflected_light_intensity
        
        if colourLeft_RLI <= target:
            largeMotor_Left.on(-speed)
            largeMotor_Right.on(speed)
            lineFound = True
            print('{} left found it'.format(colourLeft_RLI))

        if colourRight_RLI <=target:
            largeMotor_Left.on(speed)
            largeMotor_Right.on(-speed)
            print('{} right found it'.format(colourRight_RLI))

        print('{} left, {} right'.format(colourLeft_RLI, colourRight_RLI))
    
        if colourLeft_RLI == colourRight_RLI and lineFound:
            break
        if stop():
            break
    steering_drive.off()