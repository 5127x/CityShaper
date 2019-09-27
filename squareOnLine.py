def squareOnLine(speed, threshold):
    colourLeft_RLI = 0
    colourRight_RLI = 0
    lineFound = False
    steering.on(steering=0,speed=speed)
    while True:
        colourLeft_RLI = leftColour.reflected_light_intensity
        colourRight_RLI = rightColour.reflected_light_intensity
        
        if colourLeft_RLI <= threshold:
            largeMotorLeft.on(-speed)
            largeMotorRight.on(speed)
            lineFound = True
            print('{} left found it'.format(colourLeft_RLI))

        if colourRight_RLI <=threshold:
            largeMotorLeft.on(speed)
            largeMotorRight.on(-speed)
            print('{} right found it'.format(colourRight_RLI))

        print('{} left, {} right'.format(colourLeft_RLI, colourRight_RLI))
    
        if colourLeft_RLI == colourRight_RLI and lineFound:
            break