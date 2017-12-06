#########################################################################
### Date: 2017/11/9
### file name: start_linetracing.py
### Purpose: this code has been generated for start linetracing.
#########################################################################

import maze_solve
import time
import movement

# import GPIO library
import RPi.GPIO as GPIO

# set GPIO warnings as false
GPIO.setwarnings(False)

while True:
    try:
        start = time.time()
        maze_solve.maze_solve()
    except KeyboardInterrupt:
        end = time.time()
        print(end - start)
        movement.pwm_low()
        GPIO.cleanup()
        quit()