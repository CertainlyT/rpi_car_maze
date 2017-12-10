# -*- coding: utf-8 -*-
######################################################################
# Date: 2017/12/01
# file name: maze_solve.py
# Purpose: This code has been generated for define movement of
# vehicle. It contains pre-defined speed and direction.
######################################################################

import getLine
import time
import movement


def maze_solve():
    """
    This function is the main function.
    It has 4 options, (front, left, right, u_turn) , decided by flag.
    Flag 'right' means vehicle should turn right. And others are same.
    Flag is changed by go_forward_infinite function, in movement.py.
    It doesn't have return, it just set vehicle's speed and direction.
    """
    # flag - define direction
    global flag
    # initial setup
    movement.pwm_setup()
    flag = "front"
    # u_count - used for different direction of u-turn.(because of limitation of track.)
    u_count = 0
    while 1:
        line_check = getLine.get_line()
        # line tracing
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
                movement.go_forward_infinite(20, 100, line_check)
            elif line_check == ['1', '1', '1', '1', '0']:
                movement.go_forward_infinite(100, 20, line_check)
            # to avoid stop (especially when line_check is ['1', '0', '0', '0', '1'])
            else:
                movement.go_forward_infinite(50, 50, line_check)

        # right turn
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
            # return to line
            if getLine.get_line()[0] == '0' or getLine.get_line() == ['1', '1', '1', '1', '1']:
                while getLine.get_line()[1] != '0':
                    movement.leftPointTurn(40, 0.05)
            movement.stop()
            time.sleep(0.2)
            flag = "front"

        # left turn
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
            # return to line
            if getLine.get_line()[4] == '0' or getLine.get_line() == ['1', '1', '1', '1', '1']:
                while getLine.get_line()[3] != '0':
                    movement.rightPointTurn(40, 0.05)
            movement.stop()
            time.sleep(0.2)
            flag = "front"

        # u-turn
        elif flag == "u_turn":
            print(u_count)
            # to avoid going out of track.
            if u_count == 1:
                while getLine.get_line()[4] != '0':
                    movement.rightPointTurn(50, 0.01)
                # more turn
                if getLine.get_line()[4] == '0':
                    while getLine.get_line()[4] == '0':
                        movement.rightPointTurn(40, 0.05)
                movement.stop()
                time.sleep(0.2)
                # return to line
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
                # return to line
                if getLine.get_line()[4] == '0' or getLine.get_line() == ['1', '1', '1', '1', '1']:
                    while getLine.get_line()[3] != '0':
                        movement.rightPointTurn(40, 0.05)
                movement.stop()
                time.sleep(0.2)
                u_count += 1
                flag = "front"

