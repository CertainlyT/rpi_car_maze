######################################################################
### Date: 2017/11/8
### file name: movement.py
### Purpose: This code has been generated for define
###          going forward and backward.
######################################################################

# import GPIO library
import RPi.GPIO as GPIO

# import needed library
import time
import ultrasonicSensor
import getLine
import turning


# set GPIO warnings as false
GPIO.setwarnings(False)

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)

# =======================================================================
# declare the pins of 12, 11, 35 in the Raspberry Pi
# as the left motor control pins in order to control left motor
# left motor needs three pins to be controlled
# =======================================================================
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

# =======================================================================
# declare the pins of 15, 13, 37 in the Raspberry Pi
# as the right motor control pins in order to control right motor
# right motor needs three pins to be controlled
# =======================================================================
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37

# =======================================================================
# set direction
# =======================================================================

left_forward = True
left_backward = False
right_forward = False
right_backward = True


# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will
# move forward.
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH,in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# ===========================================================================
def left_motor_direction(direction):
    if direction:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    elif not direction:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    else:
        print('Config Error')


# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will
# move forward.
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH,in MotorRight_A
# and LOW to HIGH or HIGH to LOW in MotorRight_B
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH in MotorRight_A
# and LOW to HIGH or HIGH to LOW in MotorRight_B
# ===========================================================================
def right_motor_direction(direction):
    if direction:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
    elif not direction:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
    else:
        print('Config Error')


# =======================================================================
# because the connections between motors (left motor) and Raspberry Pi has been
# established, the GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================

GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

# =======================================================================
# because the connections between motors (right motor) and Raspberry Pi has been
# established, the GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================

GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

# =======================================================================
# create left pwm object to control the speed of left motor
# =======================================================================
LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)

# =======================================================================
# create right pwm object to control the speed of right motor
# =======================================================================
RightPwm = GPIO.PWM(MotorRight_PWM, 100)


# =======================================================================
#  go_forward_infinite method has been generated for the three-wheeled moving
#  object to go forward without any limitation of running_time
# =======================================================================


def avoid():
    stop()
    time.sleep(0.5)
    turning.rightPointTurn(75, 0.4)
    stop()
    time.sleep(0.5)
    go_forward(70, 1)
    stop()
    time.sleep(0.5)
    turning.leftPointTurn(75, 0.35)
    stop()
    time.sleep(0.5)
    go_forward(70, 1)
    stop()
    time.sleep(0.5)
    check = 0
    for i in range(8):
        line = getLine.get_line()
        if line != ["1", "1", "1", "1", "1"]:
            check = 1
        print(check)
        turning.leftPointTurn(60, 0.075)
    stop()
    time.sleep(0.5)
    if check == 0:
        while getLine.get_line() == ["1", "1", "1", "1", "1"]:
            go_forward(60, 0.1)
        stop()
        time.sleep(0.5)
    if getLine.get_line() != ["1", "1", "1", "1", "1"]:
        while getLine.get_line() != ["1", "1", "1", "1", "1"]:
            go_forward(70, 0.2)
        stop()
        time.sleep(0.5)
    while getLine.get_line() == ["1", "1", "1", "1", "1"]:
        turning.rightSwingTurn(70, 0.2)
    stop()
    time.sleep(0.5)


dis = 10


def go_forward_infinite(left_speed, right_speed, check_list):
    # q = Queue.Queue()
    # t = threading.Thread(target=ultrasonicSensor.measureDistance, name="SensorThread", args=[q], )
    left_motor_direction(left_forward)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    right_motor_direction(right_forward)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # to avoid collision between go_forward_any method and turn method, insert a infinite loop
    # t.start()
    while 1:
        check = getLine.get_line()
        if check != check_list:
            break
        LeftPwm.ChangeDutyCycle(left_speed)
        RightPwm.ChangeDutyCycle(right_speed)
        distance = ultrasonicSensor.measureDistance()
        if dis >= distance >= 5:
            avoid()
            break
    # t.join()


# =======================================================================
#  go_backward_infinite method has been generated for the three-wheeled moving
#  object to go backward without any limitation of running_time
# =======================================================================
def go_backward_infinite(speed):
    left_motor_direction(left_backward)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    right_motor_direction(right_backward)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # reason is as same as go_forward_any loop
    while 1:
        LeftPwm.ChangeDutyCycle(speed)
        RightPwm.ChangeDutyCycle(speed)


# =======================================================================
#  go_forward method has been generated for the three-wheeled moving
#  object to go forward with the limitation of running_time
# =======================================================================

def go_forward(speed, running_time):
    left_motor_direction(left_forward)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    right_motor_direction(right_forward)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    time.sleep(running_time)


# =======================================================================
#  go_backward method has been generated for the three-wheeled moving
#  object to go backward with the limitation of running_time
# =======================================================================

def go_backward(speed, running_time):
    left_motor_direction(left_backward)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    right_motor_direction(right_backward)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    time.sleep(running_time)


# =======================================================================
# define the stop module
# =======================================================================
def stop():
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)


# =======================================================================
# setup and initialize the left motor and right motor
# =======================================================================
def pwm_setup():
    LeftPwm.start(0)
    RightPwm.start(0)


# =======================================================================
# stop the car and cleanup gpio
# =======================================================================
def pwm_low():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()


# =======================================================================
# test code
# =======================================================================
if __name__ == "__main__":
    try:
        go_forward_infinite(60, 60, track.get_line())
        go_backward_infinite(60)
        stop()
    except KeyboardInterrupt:
        stop()