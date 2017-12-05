######################################################################
### Date: 2017/11/27
### file name: movement.py
### Purpose: This code has been generated for define
###          swing turn and point turn.
######################################################################

# import GPIO library
import RPi.GPIO as GPIO

# import needed library
import time
import getLine
import maze_solve

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

def go_forward_infinite(left_speed, right_speed, check_list):
    left_motor_direction(left_forward)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    right_motor_direction(right_forward)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    while 1:
        check = getLine.get_line()
        if check != check_list:
            check = getLine.get_line()
            if check[0] == '0' and (check[0] == '0' or check[1] == '0'):
                go_forward(55, 42, 0.4)
                if getLine.get_line() == ['1', '1', '1', '1', '1']:
                    stop()
                    time.sleep(0.5)
                    maze_solve.flag = "left"
                else:
                    pass
            elif check == ['1', '0', '0', '0', '1']:
                left = False
                right = False
                for i in range(8):
                    go_forward(57, 40, 0.05)
                    tmp = getLine.get_line()
                    if tmp[0] == '0':
                        left = True
                    if tmp[4] == '0':
                        right = True

                if left and right:
                    maze_solve.flag = "right"
                elif not left and right:
                    maze_solve.flag = "right"
                elif left and not right:
                    if getLine.get_line() == ['1', '1', '1', '1', '1']:
                        stop()
                        time.sleep(0.5)
                        maze_solve.flag = "left"
                else:
                    maze_solve.flag = "front"

            elif check == ['0', '0', '0', '0', '1']:
                go_forward(55, 42, 0.4)
                if getLine.get_line() == ['1', '1', '1', '1', '1']:
                    stop()
                    time.sleep(0.5)
                    maze_solve.flag = "left"
            elif check[4] == '0' or check == ['0', '0', '0', '0', '0']:
                go_forward(55, 42, 0.4)
                maze_solve.flag = "right"
            elif check == ['1', '1', '1', '1', '1']:
                go_forward(55, 42, 0.15)
                stop()
                time.sleep(0.5)
                if getLine.get_line() == ['1', '1', '1', '1', '1']:
                    maze_solve.flag = "u_turn"
            break
        LeftPwm.ChangeDutyCycle(left_speed)
        RightPwm.ChangeDutyCycle(right_speed)


def go_forward(left_speed, right_speed, t):
    left_motor_direction(left_forward)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    right_motor_direction(right_forward)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(left_speed)
    RightPwm.ChangeDutyCycle(right_speed)
    time.sleep(t)


# =======================================================================
# perform right point turn
# ======================================================================
def rightPointTurn(speed, running_time):
    left_motor_direction(left_forward)
    right_motor_direction(right_backward)

    # set the left and right motor pwm to be ready to movee
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go backward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the both motors to move
    time.sleep(running_time)


# ======================================================================
# perform left point turn
# ======================================================================
def leftPointTurn(speed, running_time):
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


# ======================================================================
# stop the vehicle
# ======================================================================
def stop():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)