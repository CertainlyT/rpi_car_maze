######################################################################
### Date: 2017/11/8
### file name: turning.py
### Purpose: This code has been generated for define
###          swing turn and point turn.
######################################################################

# import GPIO library
import RPi.GPIO as GPIO

# import needed library
import time

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
# perform right swing turn of 90 degree
# =======================================================================
def rightSwingTurn(speed, running_time):
    # set the right motor pwm to be ready to stop
    # Turn Off Right PWM
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # set the left motor to go forward
    left_motor_direction(left_forward)

    # set the left motor pwm to be ready to go forward
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor pwm to be ready to stop
    # Turn Off Right PWM
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to stop
    RightPwm.ChangeDutyCycle(0)
    # set the running time of the left motor to go forward
    time.sleep(running_time)


# =======================================================================
# perform left swing turn of 90 degree
# =======================================================================
def leftSwingTurn(speed, running_time):

    # set the left motor pwm to be ready to stop
    # Turn Off Left PWM
    GPIO.output(MotorLeft_PWM,GPIO.LOW)

    # set the right motor to go forward
    right_motor_direction(right_forward)

    # set the right motor pwm to be ready to go forward
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to stop
    LeftPwm.ChangeDutyCycle(0)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the right motor to go forward
    time.sleep(running_time)


# =======================================================================
# perform right point turn of 90 degree  # student assignment (1)
# ======================================================================

def rightPointTurn(speed, running_time):  # student assignment (1)
    left_motor_direction(left_forward)
    right_motor_direction(right_backward)

    # set the left and right motor pwm to be ready to move
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go backward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the both motors to move
    time.sleep(running_time)


#=======================================================================
# perform left point turn of 90 degree   # student assignment (2)
# ======================================================================

def leftPointTurn(speed, running_time):  # student assignment (2)
    right_motor_direction(right_forward)
    left_motor_direction(left_backward)

    # set the left and right motor pwm to be ready to move
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the speed of the left motor to go backward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the both motors to move
    time.sleep(running_time)


#=======================================================================
# stop the vehicle
# ======================================================================
def stop():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)