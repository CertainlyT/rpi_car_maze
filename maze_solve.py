import getLine
import time
import movement


def maze_solve():
    global flag
    movement.pwm_setup()
    flag = "front"
    u_count = 0
    while 1:
        line_check = getLine.get_line()
        if flag == "front":
            if line_check == ['1', '0', '1', '1', '1']:
                movement.go_forward_infinite(40, 100, line_check)
            elif line_check == ['1', '1', '0', '1', '1']:
                movement.go_forward_infinite(100, 100, line_check)
            elif line_check == ['1', '1', '1', '0', '1']:
                movement.go_forward_infinite(100, 40, line_check)
            elif line_check == ['0', '0', '1', '1', '1']:
                movement.go_forward_infinite(40, 100, line_check)
            elif line_check == ['1', '0', '0', '1', '1']:
                movement.go_forward_infinite(40, 100, line_check)
            elif line_check == ['1', '1', '0', '0', '1']:
                movement.go_forward_infinite(100, 40, line_check)
            elif line_check == ['1', '1', '1', '0', '0']:
                movement.go_forward_infinite(100, 40, line_check)
            elif line_check == ['0', '0', '0', '1', '1']:
                movement.go_forward_infinite(40, 100, line_check)
            elif line_check == ['1', '1', '0', '0', '0']:
                movement.go_forward_infinite(100, 40, line_check)
            elif line_check == ['0', '1', '1', '1', '1']:
                movement.go_forward_infinite(40, 100, line_check)
            elif line_check == ['1', '1', '1', '1', '0']:
                movement.go_forward_infinite(100, 40, line_check)
            else:
                movement.go_forward_infinite(50, 50, line_check)

        elif flag == "right":
            while getLine.get_line() != ['1', '1', '1', '1', '1']:
                movement.rightPointTurn(50, 0.01)
            while getLine.get_line() != ['1', '1', '1', '1', '0']:
                movement.rightPointTurn(50, 0.01)
            # more turn
            if getLine.get_line()[4] == '0':
                while getLine.get_line()[4] == '0':
                    movement.rightPointTurn(40, 0.05)
            movement.stop()
            time.sleep(0.2)
            # out
            if getLine.get_line()[0] == '0' or getLine.get_line() == ['1', '1', '1', '1', '1']:
                while getLine.get_line()[1] != '0':
                    movement.leftPointTurn(40, 0.05)
            movement.stop()
            time.sleep(0.2)
            flag = "front"

        elif flag == "left":
            while getLine.get_line() != ['1', '1', '1', '1', '1']:
                movement.leftPointTurn(50, 0.01)
            while getLine.get_line() != ['0', '1', '1', '1', '1']:
                movement.leftPointTurn(50, 0.01)
            # more turn
            if getLine.get_line()[0] == '0':
                while getLine.get_line()[0] == '0':
                    movement.leftPointTurn(40, 0.05)
            movement.stop()
            time.sleep(0.2)
            # out
            if getLine.get_line()[4] == '0' or getLine.get_line() == ['1', '1', '1', '1', '1']:
                while getLine.get_line()[3] != '0':
                    movement.rightPointTurn(40, 0.05)
            movement.stop()
            time.sleep(0.2)
            flag = "front"

        elif flag == "u_turn":
            print(u_count)
            if u_count == 1:
                while getLine.get_line()[4] != '0':
                    movement.rightPointTurn(50, 0.01)
                # more turn
                if getLine.get_line()[4] == '0':
                    while getLine.get_line()[4] == '0':
                        movement.rightPointTurn(40, 0.05)
                movement.stop()
                time.sleep(0.2)
                # out
                if getLine.get_line()[0] == '0' or getLine.get_line() == ['1', '1', '1', '1', '1']:
                    while getLine.get_line()[1] != '0':
                        movement.leftPointTurn(40, 0.05)
                u_count += 1
                movement.stop()
                time.sleep(0.2)
                flag = "front"
            else:
                while getLine.get_line()[0] != '0':
                    movement.leftPointTurn(50, 0.01)
                # more turn
                if getLine.get_line()[0] == '0':
                    while getLine.get_line()[0] == '0':
                        movement.leftPointTurn(50, 0.05)
                movement.stop()
                time.sleep(0.2)
                # out
                if getLine.get_line()[4] == '0' or getLine.get_line() == ['1', '1', '1', '1', '1']:
                    while getLine.get_line()[3] != '0':
                        movement.rightPointTurn(40, 0.05)
                movement.stop()
                time.sleep(0.2)
                u_count += 1
                flag = "front"

