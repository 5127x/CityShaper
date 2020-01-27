#!/usr/bin/env python3

# Import the EV3-robot library
import ev3dev.ev3 as ev3
from time import sleep



# Constructor

btn = ev3.Button()    
shut_down = False

# Main method
def run():

    # sensors
    cs = ev3.ColorSensor('in2');      assert cs.connected  # measures light intensity
    shut_down = False

    cs.mode = 'COL-REFLECT'  # measure light intensity


    # motors
    lm = ev3.LargeMotor('outB');  assert lm.connected  # left motor
    rm = ev3.LargeMotor('outC');  assert rm.connected  # right motor
    mm = ev3.MediumMotor('outD'); assert mm.connected  # medium motor

    speed = 360/4  # deg/sec, [-1000, 1000]
    dt = 500       # milliseconds
    stop_action = "coast"

    # PID tuning
    Kp = 1  # proportional gain
    Ki = 0  # integral gain
    Kd = 0  # derivative gain

    integral = 0
    previous_error = 0

    # initial measurment
    target_value = cs.value()

    # Start the main loop
    while not shut_down:

        # deal with obstacles


        # Calculate steering using PID algorithm
        error = target_value - cs.value()
        integral += (error * dt)
        derivative = (error - previous_error) / dt

        # u zero:     on target,  drive forward
        # u positive: too bright, turn right
        # u negative: too dark,   turn left

        u = (Kp * error) + (Ki * integral) + (Kd * derivative)

        # limit u to safe values: [-1000, 1000] deg/sec
        if speed + abs(u) > 1000:
            if u >= 0:
                u = 1000 - speed
            else:
                u = speed - 1000

        # run motors
        if u >= 0:
            lm.run_timed(time_sp=dt, speed_sp=speed + u, stop_action=stop_action)
            rm.run_timed(time_sp=dt, speed_sp=speed - u, stop_action=stop_action)
            sleep(dt / 1000)
        else:
            lm.run_timed(time_sp=dt, speed_sp=speed - u, stop_action=stop_action)
            rm.run_timed(time_sp=dt, speed_sp=speed + u, stop_action=stop_action)
            sleep(dt / 1000)

        previous_error = error

        # Check if buttons pressed (for pause or stop)
        if btn.down:  # Stop
            print("Exit program... ")
            shut_down = True
        elif not btn.left:  # Pause
            print("[Pause]")
            pause()

# 'Pause' method
def pause(pct=0.0, adj=0.01):
    while btn.right or btn.left:  # ...wait 'right' button to unpause
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER, pct)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.AMBER, pct)
        if (pct + adj) < 0.0 or (pct + adj) > 1.0:
            adj = adj * -1.0
        pct = pct + adj

    print("[Continue]")
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)


# Main function
#if __name__ == "__main__":
run()