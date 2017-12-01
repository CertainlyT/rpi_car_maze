import getLine
import time
import movement


def maze_solve():
    global flag
    movement.pwm_setup()
    flag = "front"
    while 1:
        line_check = getLine.get_line()
        if flag == "front":
            if line_check == ['1', '0', '1', '1', '1']:
                movement.go_forward_infinite(20, 70, line_check)
            elif line_check == ['1', '1', '0', '1', '1']:
                movement.go_forward_infinite(70, 70, line_check)
            elif line_check == ['1', '1', '1', '0', '1']:
                movement.go_forward_infinite(70, 20, line_check)
            elif line_check == ['0', '0', '1', '1', '1']:
                movement.go_forward_infinite(25, 100, line_check)
            elif line_check == ['1', '0', '0', '1', '1']:
                movement.go_forward_infinite(30, 80, line_check)
            elif line_check == ['1', '1', '0', '0', '1']:
                movement.go_forward_infinite(80, 30, line_check)
            elif line_check == ['1', '1', '1', '0', '0']:
                movement.go_forward_infinite(100, 25, line_check)
            elif line_check == ['0', '0', '0', '1', '1']:
                movement.go_forward_infinite(10, 95, line_check)
            elif line_check == ['1', '1', '0', '0', '0']:
                movement.go_forward_infinite(95, 10, line_check)
        elif flag == "right":
            movement.go_forward(50, 42, 0.4)
            movement.stop()
            time.sleep(0.5)
            while getLine.get_line() != ['1', '1', '1', '1', '1']:
                movement.rightPointTurn(40, 0.05)
            while getLine.get_line() != ['1', '1', '1', '1', '0']:
                movement.rightPointTurn(40, 0.05)
            if getLine.get_line()[4] == '0':
                movement.rightPointTurn(40, 0.15)
            movement.stop()
            time.sleep(0.5)
            flag = "front"
        elif flag == "left":
            while getLine.get_line() != ['1', '1', '1', '1', '1']:
                movement.leftPointTurn(50, 0.05)
            while getLine.get_line() != ['0', '1', '1', '1', '1']:
                movement.leftPointTurn(50, 0.05)
            if getLine.get_line()[0] == '0':
                movement.leftPointTurn(40, 0.15)
            movement.stop()
            time.sleep(0.5)
            flag = "front"
        elif flag == "u_turn":
            movement.stop()
            time.sleep(0.5)
            while getLine.get_line() != ['1', '1', '1', '1', '0']:
                movement.rightPointTurn(40, 0.05)
            if getLine.get_line()[4] == '0':
                movement.rightPointTurn(40, 0.15)
            movement.stop()
            time.sleep(0.5)
            flag = "front"


