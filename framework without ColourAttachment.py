#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

from delayForSeconds import delayForSeconds
from squareOnLine import squareOnLine
from Turn_degrees import Turn_degrees
from Straight_gyro import Straight_gyro
from onForRotations import onForRotations
from onForSeconds import onForSeconds
from Steering_rotations import Steering_rotations
from Steering_seconds import Steering_seconds
from Stopping_on_black_line import Stopping_on_black_line
from reset_gyro import reset_gyro

print("Hello!", file=stderr)

colourLeft = ColorSensor(INPUT_3) # bcs apparently they have to be backwards...
colourRight = ColorSensor(INPUT_2)
gyro = GyroSensor(INPUT_1)

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)

largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
# mediumMotor_Left = MediumMotor(OUTPUT_A)
mediumMotor = MediumMotor(OUTPUT_D)

def isRobotLifted():
    return colourLeft.reflected_light_intensity < 2 # colourLeft.raw[0] < 5 and colourLeft.raw[1] < 5 and colourLeft.raw[2] < 5

def launchStep(stop, action):
    name = action.get('action')

    if name == 'onForSeconds': # (stop, motor, speed, seconds, brake)
        motor = action.get('motor')
        speed = float(action.get('speed'))
        seconds = float(action.get('seconds'))
        brake = bool(action.get('brake'))
        if (motor == "largeMotor_Left"):
            motorToUse = largeMotor_Left
        if (motor == "largeMotor_Right"):
            motorToUse = largeMotor_Right
        # if (motor == "mediumMotor_Left"): motorToUse = mediumMotor_Left
        if (motor == "mediumMotor"):
            motorToUse = mediumMotor
        thread = threading.Thread(target=onForSeconds, args=(stop, motorToUse, speed, seconds, brake))
        thread.start()
        return thread
    
    if name == 'onForRotations': # (stop, motor, speed, rotations, brake)
        print("onForRotations", file=stderr)
        motor = action.get('motor')
        speed = float(action.get('speed'))
        rotations = float(action.get('rotations'))
        brake = bool(action.get('brake'))
        if (motor == "largeMotor_Left"):
            motorToUse = largeMotor_Left
        if (motor == "largeMotor_Right"):
            motorToUse = largeMotor_Right
        #if (motor == "mediumMotor_Left"): motorToUse = mediumMotor_Left
        if (motor == "mediumMotor"):
            motorToUse = mediumMotor
        thread = threading.Thread(target=onForRotations, args=(stop, motorToUse, speed, rotations, brake))
        thread.start()
        return thread

    if name == 'Steering_seconds': # (stop, speed, seconds, steering, brake)
        speed = float(action.get('speed'))
        seconds = float(action.get('seconds'))
        steering = float(action.get('steering'))
        brake = bool(action.get('brake'))
        thread = threading.Thread(target=Steering_seconds, args= (stop, speed, steering, brake))
        thread.start()
        return thread

    if name == 'Steering_rotations': # (stop, speed, rotations, steering, brake)
        speed = float(action.get('speed'))
        rotations = float(action.get('rotations'))
        steering = float(action.get('steering'))
        brake = bool(action.get('brake'))
        thread = threading.Thread(target=Steering_rotations, args=(stop, speed, rotations, steering, brake))
        thread.start()
        return thread

    if name == 'delayForSeconds': # (stop, seconds)
        print("delayForSeconds", file=stderr)
        seconds = float(action.get('seconds'))
        thread = threading.Thread(target=delayForSeconds, args=(stop, seconds))
        thread.start()
        return thread

    if name == 'squareOnLine': # (stop, speed, target)
        speed = float(action.get('speed'))
        target = float(action.get('target'))
        thread = threading.Thread(target=squareOnLine, args=(stop, speed, target))
        thread.start()
        return thread
    
    if name == 'Turn_degrees': # (stop, speed, degrees)
        speed = float(action.get('speed'))
        degrees = float(action.get('degrees'))
        thread = threading.Thread(target = Turn_degrees, args=(stop, speed, degrees))
        thread.start()
        return thread

    if name == 'Straight_gyro': # (stop, speed, rotations)
        print("Straight_gyro", file=stderr)
        speed = float(action.get('speed'))
        rotations = float(action.get('rotations'))
        thread = threading.Thread(target=Straight_gyro, args=(stop, speed, rotations))
        thread.start()
        return thread

    if name == 'Stopping_on_black_line': # stop, rotations, speed, LineSide, colourSensor
        rotations = float(action.get('rotations'))
        speed = float(action.get('speed'))
        LineSide = action.get('LineSide')
        colourSensor = action.get('colourSensor')
        thread = threading.Thread(target = Stopping_on_black_line, args=(stop, rotations, speed, LineSide, colourSensor))
        thread.start()
        return thread

    if name == 'reset_gyro': 
        thread = threading.Thread(target=reset_gyro)
        thread.start()
        return thread

def main():
    threadPool = []
    actions = []
    stopProcessing = False
    programXML = ET.parse('programming_test.xml')
    programs = programXML.getroot()
    mediumMotor.reset # could be the other motor
    steps = programXML.getroot()
    for step in steps:
        action = step.get('action')
        # are their multiple actions to execute in parallel?
        if action == 'launchInParallel':
            for subSteps in step:
                thread = launchStep(lambda:stopProcessing, subSteps)
                threadPool.append(thread)
        # is there a single action to execute?
        else:
            thread = launchStep(lambda:stopProcessing, step)
            threadPool.append(thread)
        while not stopProcessing:
            # remove any completed threads from the pool
            for thread in threadPool:
                if not thread.isAlive():
                    threadPool.remove(thread)
            # if there are no threads running, exist the 'while' loop 
            # and start the next action from the list 
            if not threadPool:
                break
            # if the robot has been lifted then complete everything
            if isRobotLifted():
                stopProcessing = True
                break
            #sleep(0.25)
        # if the 'stopProcessing' flag has been set then finish the step loop
        if stopProcessing:
            break
gyro.mode = 'GYRO-ANG'
gyro.mode = 'GYRO-RATE'
gyro.mode = 'GYRO-ANG'
main()