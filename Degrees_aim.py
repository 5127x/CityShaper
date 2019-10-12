
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
from sys import stderr
#steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
gyro = GyroSensor(INPUT_1)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)


def turn_to_degrees(stop, speed, degrees, direction):
    print("In turn_to_degrees", file=stderr)
    current_gyro_reading = gyro.angle
    print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)
    if direction == "RIGHT":    
        while (float(current_gyro_reading) < float(degrees)):
            print("Current Gyro: {}".format (float(current_gyro_reading)))
            tank_block.on(right_speed = -speed, left_speed = speed)
            current_gyro_reading = gyro.angle
            if stop():
                break
        
    else:    
        print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)
        if current_gyro_reading > degrees:
            tank_block.on(right_speed = speed, left_speed = -speed)
            while (float(current_gyro_reading) > float(degrees)):
                print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)
                current_gyro_reading = gyro.angle
                if stop():
                    break
        elif current_gyro_reading < degrees:
            tank_block.on(right_speed = speed, left_speed = -speed)
            while (float(current_gyro_reading) < float(degrees)):
                print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)
                current_gyro_reading = gyro.angle
                if stop():
                    break
    tank_block.off
    print("Leaving turn_to_degrees", file=stderr)        
    print("Current Gyro: {}".format (float(current_gyro_reading)), file=stderr)

#turn_to_degrees(100, 60, "RIGHT")
#turn_to_degrees(100, -45, "LEFT")
#stopProcessing = False
#turn_to_degrees(lambda:stopProcessing, 100, 96, "RIGHT")

        

        
        
        


        