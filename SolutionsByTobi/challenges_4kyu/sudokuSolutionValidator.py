########################################################################
#                                                                      #
#   NAME:     Sudoku Solution Validator                                #
#   RANK:     4kyu                                                     #
#   URL:      https://www.codewars.com/kata/529bf0e9bdf7657179000008   #
#                                                                      #
########################################################################

import numpy as np


def valid_solution(board):
    board = np.array(board)
    boxes = np.array([board[3 * x:3 * x + 3, 3 * y:3 * y + 3] for x in range(3) for y in range(3)])
    for row in [*board, *board.transpose(), *boxes.reshape(9, 9)]:  # board: rows, board.transpose(): columns, boxes: boxes of the sudoku grid
        if len(row) != len(set(row)):
            return False
    return True
