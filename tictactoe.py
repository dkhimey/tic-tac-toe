"""
Tic Tac Toe Player
"""

import math
import numpy as np

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
    num_board = numerical_board(board)
    if np.sum(num_board)==1:
        return O
    if np.sum(num_board)==0:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
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
        if np.sum(num_board[row])==-3:
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
    if winner(board)==X or winner(board)==O:
        return True

    elif np.any(num_board!=0):
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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
