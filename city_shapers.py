#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time
from sys import stderr

# import the functions 

from Do_nothing import Do_nothing
from off import off
from Delay_seconds import Delay_seconds

from Motor_onForRotations import Motor_onForRotations
from Motor_onForSeconds import Motor_onForSeconds
from Steering_rotations import Steering_rotations
from Steering_seconds import Steering_seconds
from Tank_rotations import Tank_rotations
from Tank_seconds import Tank_seconds

from Reset_gyro import Reset_gyro
from Straight_gyro import Straight_gyro
from Turn_degrees import Turn_degrees
from Turn_from_start_position import Turn_from_start_position

from squareOnLine import squareOnLine
from FollowBlackLine_rotations import FollowBlackLine_rotations
from LookingBlackLine_stopBlack import LookingBlackLine_stopBlack
from LookingBlackLine_rotations import LookingBlackLine_rotations

print("STARTED!", file=stderr)

# define the different sensors, motors and motor blocks
colourAttachment = ColorSensor(INPUT_4)
colourLeft = ColorSensor(INPUT_3) 
colourRight = ColorSensor(INPUT_2)
gyro = GyroSensor(INPUT_1)

largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
mediumMotor = MediumMotor(OUTPUT_D)

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_block = MoveTank(OUTPUT_B, OUTPUT_C)


def isRobotLifted(): # has the robot been lifted?
    # return true if the robot was lifted and stop the motors IF we are not doing run5
    # driving over the gaps in bridge can accidently trigger isRobotLifted()
    if fileName != 'programming_run_5.xml':
         off()
         return colourLeft.reflected_light_intensity < 2 
        # alternate values: colourLeft.raw[0] < 5 and colourLeft.raw[1] < 5 and colourLeft.raw[2] < 5

def isKeyTaken(): # has the key been removed?
    # return True if the key was removed and stop the motors 
    rbgA = colourAttachment.raw
    off()
    # rgb values are 50, 62, 57 when the slot is empty
    return abs(rbgA[0] - 50) < 10 and abs(rbgA[1] - 62) < 10 and abs(rbgA[2] - 57) < 10 

# launch actions using threads
def launchStep(stop, action):

    # compare the 'name' to our functions and start a thread with the matching function
    # return the thread to add to threadPool
    name = action.get('action')

    if name == 'Do_nothing': # (stop)
        print("Do_nothing", file= stderr)
        thread = threading.Thread(target=Do_nothing, args=(stop,))
        thread.start()
        return thread

    if name == 'off': # ()
        print("Motors off", file=stderr)
        thread = threading.Thread(target=off)
        thread.start()
        return thread

    if name == 'Delay_seconds': # (stop, seconds)
        print("Starting Delay_seconds", file=stderr)
        seconds = float(action.get('seconds'))
        thread = threading.Thread(target=Delay_seconds, args=(stop, seconds))
        thread.start()
        return thread

    if name == 'Motor_onForRotations': # (stop, motor, speed, rotations, gearRatio)
        print("Starting Motor_onForRotations", file=stderr)
        motor = action.get('motor')
        speed = float(action.get('speed'))
        rotations = float(action.get('rotations'))
        gearRatio = float(action.get('gearRatio'))
        if (motor == "largeMotor_Left"):
            motorToUse = largeMotor_Left
        if (motor == "largeMotor_Right"):
            motorToUse = largeMotor_Right
        if (motor == "mediumMotor"):
            motorToUse = mediumMotor
        thread = threading.Thread(target=Motor_onForRotations, args=(stop, motorToUse, speed, rotations, gearRatio))
        thread.start()
        return thread

    if name == 'Motor_onForSeconds': # (stop, motor, speed, seconds)
        print("Starting Motor_onForSeconds", file=stderr)
        motor = action.get('motor')
        speed = float(action.get('speed'))
        seconds = float(action.get('seconds'))
        if (motor == "largeMotor_Left"):
            motorToUse = largeMotor_Left
        if (motor == "largeMotor_Right"):
            motorToUse = largeMotor_Right
        if (motor == "mediumMotor"):
            motorToUse = mediumMotor
        thread = threading.Thread(target=Motor_onForSeconds, args=(stop, motorToUse, speed, seconds))
        thread.start()
        return thread
    
    if name == 'Steering_rotations': # (stop, speed, rotations, steering)
        print("Starting Steering_rotations", file=stderr)
        speed = float(action.get('speed'))
        rotations = float(action.get('rotations'))
        steering = float(action.get('steering'))
        brake = bool(action.get('brake'))
        thread = threading.Thread(target=Steering_rotations, args=(stop, speed, rotations, steering, brake))
        thread.start()
        return thread
    
    if name == 'Steering_seconds': # (stop, speed, seconds, steering)
        print("Starting Steering_seconds", file=stderr)
        speed = float(action.get('speed'))
        seconds = float(action.get('seconds'))
        steering = float(action.get('steering'))
        thread = threading.Thread(target=Steering_seconds, args= (stop, speed, steering))
        thread.start()
        return thread

    if name == 'Tank_rotations': # (stop, left_speed, right_speed, rotations)
        print("Starting Tank_rotations", file=stderr)
        left_speed = float(action.get('left_speed'))
        right_speed = float(action.get('right_speed'))
        rotations = float(action.get('rotations'))
        thread = threading.Thread(target = Tank_rotations, args=(stop, left_speed, right_speed, rotations))
        thread.start()
        return thread

    if name == 'Tank_seconds': # (stop, left_speed, right_speed, seconds)
        print("Starting Tank_seconds", file=stderr)
        left_speed = float(action.get('left_speed'))
        right_speed = float(action.get('right_speed'))
        seconds = float(action.get('seconds'))
        thread = threading.Thread(target = Tank_seconds, args=(stop, left_speed, right_speed, seconds))
        thread.start()
        return thread

    if name == 'Reset_gyro': # ()
        print("Starting Reset_gyro", file=stderr)
        thread = threading.Thread(target=Reset_gyro)
        thread.start()
        return thread

    if name == 'Straight_gyro': # (stop, speed, rotations)
        print("Starting Straight_gyro", file=stderr)
        speed = float(action.get('speed'))
        rotations = float(action.get('rotations'))
        thread = threading.Thread(target=Straight_gyro, args=(stop, speed, rotations))
        thread.start()
        return thread
    
    if name == 'Turn_degrees': # (stop, speed, degrees)
        print("Starting Turn_degrees", file=stderr)
        speed = float(action.get('speed'))
        degrees = float(action.get('degrees'))
        thread = threading.Thread(target = Turn_degrees, args=(stop, speed, degrees))
        thread.start()
        return thread

    if name == 'Turn_from_start_position': # (stop, speed, degrees)
        print('Starting Turn_from_start_position', file=stderr)
        speed = float(action.get('speed'))
        degrees = float(action.get('degrees'))
        thread = threading.Thread(target = Turn_from_start_position, args=(stop, speed, degrees))
        thread.start()
        return thread

    if name == 'squareOnLine': # (stop, speed, target)
        print("Starting squareOnLine", file=stderr)
        speed = float(action.get('speed'))
        target = float(action.get('target'))
        thread = threading.Thread(target=squareOnLine, args=(stop, speed, target))
        thread.start()
        return thread

    if name == 'FollowBlackLine_rotations': # (stop, rotations, speed, colourSensor)
        print("Starting FollowBlackLine_rotations", file=stderr)
        rotations = float(action.get('rotations'))
        speed = float(action.get('speed'))
        colourSensor = action.get('colourSensor')
        thread = threading.Thread(target = FollowBlackLine_rotations, args=(stop, rotations, speed, colourSensor))
        thread.start()
        return thread

    if name == 'LookingBlackLine_rotations': # (stop, rotations, speed, colourSensor)
        print('Starting LookingBlackLine_rotations', file=stderr)
        rotations = float(action.get('rotations'))
        speed = float(action.get('speed'))
        colourSensor = action.get('colourSensor')
        thread = threading.Thread(target = LookingBlackLine_rotations, args=(stop, rotations, speed, colourSensor))
        thread.start()
        return thread

    if name == 'LookingBlackLine_stopBlack': # (stop, rotations, speed, colourSensor)
        print('Starting LookingBlackLine_stopBlack', file=stderr)
        rotations = float(action.get('rotations'))
        speed = float(action.get('speed'))
        colourSensor = action.get('colourSensor')
        thread = threading.Thread(target = LookingBlackLine_stopBlack, args=(stop, rotations, speed, colourSensor))
        thread.start()
        return thread

# main section of the program
def main():
    # create dictionaries and variables
    threadPool = []
    actions = []
    stopProcessing = False
    # open and read the overall XML file 
    programXML = ET.parse('overall_programming.xml')
    programs = programXML.getroot()
    while True:
        # reset stopProcessing each repetition
        stopProcessing = False
        # collect the raw rgb light values from colourAttachment and the overall XML file
        # compare the sets of values
        rgb = colourAttachment.raw
        for program in programs:
            programName = program.get('name')
            rProgram = int(program.get('r'))
            gProgram = int(program.get('g'))
            bProgram = int(program.get('b'))
            rColourSensor = rgb[0]
            gColourSensor = rgb[1]
            bColourSensor = rgb[2]
            print("R {} G {} B {}").format (rColourSensor, gColourSensor, bColourSensor)
            # if the values match, run the corresponding program
            if abs(rColourSensor - rProgram) < 10 and abs(gColourSensor - gProgram) < 10 and abs(bColourSensor - bProgram) < 10:
                mediumMotor.reset 
                # read the relevant program XML
                fileName = program.get('fileName')
                print(fileName,file=stderr)
                dataXML = ET.parse(fileName)
                steps = dataXML.getroot()
                # run each step individually unless they are run in parallel
                for step in steps:
                    action = step.get('action')
                    # loop through actions that should be run in parallel
                    if action == 'launchInParallel':
                        for subSteps in step:
                            thread = launchStep(lambda:stopProcessing, subSteps)
                            threadPool.append(thread)
                    # run each action that isn't run in parrallel idividually
                    else:
                        thread = launchStep(lambda:stopProcessing, step)
                        threadPool.append(thread)
                    while not stopProcessing:
                        # remove any completed threads from the pool
                        for thread in threadPool:
                            if not thread.isAlive():
                                threadPool.remove(thread)
                        # if there are no threads running start the next action
                        if not threadPool:
                            break
                        # if the robot has been lifted or the key removed then stop everything
                        if isRobotLifted():
                            stopProcessing = True
                            break
                        if isKeyTaken():
                            stopProcessing = True
                            break
                    # if the 'stopProcessing' flag has been set then finish the whole loop
                    if stopProcessing:
                        break

main()