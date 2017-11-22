import RPi.GPIO as GPIO

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# set up GPIO mode as BOARD
# =======================================================================
GPIO.setmode(GPIO.BOARD)

# =======================================================================
# declare the pins of 16, 18, 22, 40, 32 in the Raspberry Pi
# as the control pins of 5-way tracking sensor in order to
# control direction
#
#  leftTwo    leftOne     center     rightOne     rightTwo
#    16          18         22          40           32
#
# led turns on (1) : tracking sensor led detects white playground
# led turns off(0) : tracking sensor led detects black line

# leftTwo off : it means that moving object finds black line
#                   at the position of leftTwo
#                   black line locates below the leftTwo of the moving object
#
# leftOne off : it means that moving object finds black line
#                   at the position of leftOne
#                   black line locates below the leftOne of the moving object
#
# center off : it means that moving object finds black line
#                   at the position of center
#                   black line locates below the center of the moving object
#
# rightOne off : it means that moving object finds black line
#                   at the position of rightOne
#                   black line locates below the rightOne  of the moving object
#
# rightTwo off : it means that moving object finds black line
#                   at the position of rightTwo
#                   black line locates below the rightTwo of the moving object
# =======================================================================

leftTwo = 16
leftOne = 18
center = 22
rightOne = 40
rightTwo = 32


# =======================================================================
# because the connections between 5-way tracking sensor and Raspberry Pi has been
# established, the GPIO pins of Raspberry Pi
# such as leftTwo, leftOne, center, rightOne, and rightTwo
# should be clearly declared whether their roles of pins
# are output pin or input pin
# since the 5-way tracking sensor data has been detected and
# used as the input data, leftTwo, leftOne, center, rightOne, and rightTwo
# should be clearly declared as input
#
# =======================================================================

GPIO.setup(leftTwo, GPIO.IN)
GPIO.setup(leftOne, GPIO.IN)
GPIO.setup(center,   GPIO.IN)
GPIO.setup(rightOne, GPIO.IN)
GPIO.setup(rightTwo, GPIO.IN)


def get_line():
    line_status = [str(GPIO.input(leftTwo)), str(GPIO.input(leftOne)), str(GPIO.input(center)),
                   str(GPIO.input(rightOne)), str(GPIO.input(rightTwo))]
    return line_status
