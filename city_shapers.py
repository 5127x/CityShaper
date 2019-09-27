#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor, INPUT_1, INPUT_2, INPUT_3, INPUT_4
import xml.etree.ElementTree as ET
import threading
import time

colourAttachment = ColorSensor(INPUT_4)
colourLeft = ColorSensor(INPUT_2)
colourRight = ColorSensor(INPUT_3)
gyro = GyroSensor(INPUT_1)
largeMotor_Left= LargeMotor(OUTPUT_B)
largeMotor_Right= LargeMotor(OUTPUT_C)
mediumMotor_Left = MediumMotor(OUTPUT_A)
mediumMotor_Right = MediumMotor(OUTPUT_D)

def isRobotLifted():
    return colourLeft.raw[0] < 5 and colourLeft.raw[1] < 5 and colourLeft.raw[2] < 5


def onForSeconds(stop, motor, speed, seconds):
    start_time = time.time()
    motor.on(speed, brake = True, block = False)
    while time.time() < start_time + seconds:
        if stop():
            break
    motor.off()


def delayForSeconds(stop, seconds):
    start_time = time.time()
    while time.time() < start_time + seconds:
        if stop():
            break
'''
def launchStep(stop, action):
    name = action.get('action')
    motor = action.get('motor')
    speed = float(action.get('speed'))
    seconds = float(action.get('seconds'))

    if name == 'onForSeconds':
        if (motor == "largeMotor_Left"):
            motorToUse = largeMotor_Left
        if (motor == "largeMotor_Right"):
            motorToUse = largeMotor_Right
        if (motor == "mediumMotor"):
            motorToUse = mediumMotor
        thread = threading.Thread(target=onForSeconds, args=(stop, motorToUse, speed, seconds))
        thread.start()
        return thread
    
    if name == 'delayForSeconds':
        thread = threading.Thread(target=delayForSeconds, args=(stop, seconds))
        thread.start()
        return thread
'''

def launchStep(stop, action):
    name = action.get('action')

    if name == 'onForSeconds':
        motor = action.get('motor')
        speed = float(action.get('speed'))
        seconds = float(action.get('seconds'))
        if (motor == "largeMotor_Left"):
            motorToUse = largeMotor_Left
        if (motor == "largeMotor_Right"):
            motorToUse = largeMotor_Right
        if (motor == "mediumMotor_Left"):
            motorToUse = mediumMotor_Left
        if (motor == "mediumMotor_Right"):
            motorToUse = mediumMotor_Right
        thread = threading.Thread(target=onForSeconds, args=(stop, motorToUse, speed, seconds))
        thread.start()
        return thread
    
    if name == 'onForRotations':
        motor = action.get('motor')
        speed = float(action.get('speed'))
        rotations = float(action.get('rotations'))
        if (motor == "largeMotor_Left"):
            motorToUse = largeMotor_Left
        if (motor == "largeMotor_Right"):
            motorToUse = largeMotor_Right
        if (motor == "mediumMotor_Left"):
            motorToUse = mediumMotor_Left
        if (motor == "mediumMotor_Right"):
            motorToUse = mediumMotor_Right
        thread = threading.Thread(target=onForSeconds, args=(stop, motorToUse, speed, rotations))
        thread.start()
        return thread

    if name == 'delayForSeconds':
        seconds = float(action.get('seconds'))
        thread = threading.Thread(target=delayForSeconds, args=(stop, seconds))
        thread.start()
        return thread

def main():
    threadPool = []
    actions = []
    stopProcessing = False
    cl = ColorSensor(colourAttachment)
    programXML = ET.parse('overall_programming.xml')
    programs = programXML.getroot()
    while True:
        rgb = cl.raw
        for program in programs:
            programName = program.get('name')
            rProgram = int(program.get('r'))
            gProgram = int(program.get('g'))
            bProgram = int(program.get('b'))
            rColourSensor = rgb[0]
            gColourSensor = rgb[1]
            bColourSensor = rgb[2]
            if abs(rColourSensor - rProgram) < 20 and abs(gColourSensor - gProgram) < 20 and abs(bColourSensor - bProgram) < 20:
                fileName = program.get('fileName')
                dataXML = ET.parse(fileName)
                steps = dataXML.getroot()
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

main()