# -*- coding: utf-8 -*-
#########################################################################
# Date: 2017/12/01
# file name: start_maze_solve.py
# Purpose: this code has been generated for start the main function.
#########################################################################

# import needed modules
import sys
import time
import maze_solve
import movement

# import GPIO library
import RPi.GPIO as GPIO

# set GPIO warnings as false
GPIO.setwarnings(False)

while True:
    # infinite loop while not KeyboardInterrupt.
    try:
        # check time
        start = time.time()
        maze_solve.maze_solve()
    except KeyboardInterrupt:
        end = time.time()
        # check time
        print(end - start)
        # for clean shutdown
        movement.pwm_low()
        GPIO.cleanup()
        sys.exit()