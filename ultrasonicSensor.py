######################################################################
### Date: 2017/11/8
### file name: ultrasonicSensor.py
### Purpose: this code has generated for the return
###         the distance between the moving object and obstacle
###         ultra sensor
######################################################################

import RPi.GPIO as GPIO  # import GPIO library
import time  # import needed library
import Queue

GPIO.setmode(GPIO.BOARD)

trig = 33
echo = 31

# ultrasonic sensor setting
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)


# get distance using ultra wave sensor
def measureDistance():
    GPIO.output(trig, False)
    # time.sleep(0.1)  # modified to 0.1 for detailed measurement
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    pulse_start = 0
    pulse_end = 0
    while GPIO.input(echo) == 0:
        pulse_start = time.time()
    while GPIO.input(echo) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    print(distance)
    distance = round(distance, 2)
    return distance
    # return_args = distance
    # queue.put(return_args)


if __name__ == "__main__":
    q = Queue.Queue()
    while 1:
        print(measureDistance(q))