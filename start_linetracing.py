#########################################################################
### Date: 2017/11/9
### file name: start_linetracing.py
### Purpose: this code has been generated for start linetracing.
#########################################################################

import tracingModule
import movement
import sys

# import GPIO library
import RPi.GPIO as GPIO

# set GPIO warnings as false
GPIO.setwarnings(False)

while True:
    try:
        tracingModule.line_tracing()
    except KeyboardInterrupt:
        movement.pwm_low()
        GPIO.cleanup()
        sys.exit()