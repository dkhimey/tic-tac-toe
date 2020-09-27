"""
Tic Tac Toe Player
"""

import math
import numpy as np
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def numerical_board(board):
    """
    Returns a board where X=1, O=-1, EMPTY=0, as a numpy array.
    """
    for row in range(3):
        for value in range(3):
            if board[row][value] == X:
                board[row][value] = 1
            if board[row][value] == None:
                board[row][value] = 0
            if board[row][value] == O:
                board[row][value] = -1
    return np.array(board)

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # raise NotImplementedError
    board = copy.deepcopy(board)
    num_board = numerical_board(board)
    if np.sum(num_board)==1:
        return O
    if np.sum(num_board)==0:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    board = copy.deepcopy(board)

    num_board = numerical_board(board)

    actions = set()

    for row in range(3):
        for cell in range(3):
            if num_board[row][cell]==0:
                actions.add((row,cell))

    if np.all(num_board!=0):
        return None

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    result_board = copy.deepcopy(board)

#     determine what symbol will be placed
    symbol = player(result_board)

    move = action

    row = move[0]
    cell = move[1]

    if symbol == 'X':
        result_board[row][cell]=X

    if symbol == 'O':
        result_board[row][cell]=O

    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    board = copy.deepcopy(board)

    num_board = numerical_board(board)
    #   check rows for winner
    for row in range(3):
        if np.sum(num_board[row])==3:
            return X
        if np.sum(num_board[row])==-3:
            return O
#   check columns for winner
    for column in range(3):
        if np.sum(num_board.T[column])==3:
            return X
        if np.sum(num_board.T[column])==-3:
            return O
#   check diagonals for winner:
    if np.sum(np.diagonal(num_board))==3:
        return X
    if np.sum(np.diagonal(num_board))==-3:
        return O
    if np.sum(np.fliplr(num_board).diagonal())==3:
        return X
    if np.sum(np.fliplr(num_board).diagonal())==-3:
        return O

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    board = copy.deepcopy(board)

    num_board = numerical_board(board)

    if winner(board)==X or winner(board)==O:
        return True

    elif np.all(num_board!=0):
        return True

    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    if winner(board)==O:
        return -1
    if winner(board)==None:
        return 0

# def max_value(board):
#     if terminal(board):
#         return utility(board)
#     v = -np.inf
#
#     for action in actions(board):
#         v = max(v, min_value(result(board,action)))
#
#     return action
#
# def min_value(board):
#     if terminal(board):
#         return utility(board)
#     v = np.inf
#
#     for action in actions(board):
#         v = min(v, max_value(result(board,action)))
#         move =
#
#     return action
def max_value(board):
    if terminal(board):
        return (None, utility(board))
    value = float("-inf")
    move = None
    for action in actions(board):
        v = min_value(result(board, action))[1]
        if v > value:
            value = v
            move = action
    return (move, value)

def min_value(board):
    if terminal(board):
        return (None, utility(board))
    value = float("inf")
    move = None
    for action in actions(board):
        v = max_value(result(board, action))[1]
        if v < value:
            value = v
            move = action
    return (move, value)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)

    if terminal(board):
        return none

    if board == initial_state():
        return (np.random.randint(0,3), np.random.randint(0,3))

    if turn==X:
        return max_value(board)[0]
    if turn==O:
        return min_value(board)[0]
