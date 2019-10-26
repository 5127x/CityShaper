from ev3dev2.motor import  LargeMotor, MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep
from sys import stderr
#_______________________________________________________________________________
    
colorLeft = ColorSensor(INPUT_3)
colorRight = ColorSensor(INPUT_2)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
largeMotor_Left = LargeMotor(OUTPUT_B)
largeMotor_Right = LargeMotor(OUTPUT_C)
rotations = rotations * 360
current_rotations = largeMotor_Left.position
target_RLI = 69
number = 0
total_RLI = 0

for x in range (10):
    steering_drive.on(speed = 10)
    current_RLI = colorRight.reflected_light_intensity
    number = number +1
    total_RLI = float(current_RLI) + float(total_RLI)
    Average = float(total_RLI)/number

    print(Average, file = stderr)

motor.off()

