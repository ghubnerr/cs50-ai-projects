"""
Tic Tac Toe Player
"""
import copy
import math

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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_plays = 0
    for row in board:
        for num in row:
            if num:
                num_plays += 1
    if num_plays % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_available = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions_available.add((i, j))

    return actions_available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    move = player(board)

    new_board = copy.deepcopy(board)

    if board[i][j]:
        raise Exception('Invalid Action')
    else:
        new_board[i][j] = move

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0]:
                return row[0]

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i]:
                return board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0]:
            return board[0][0]

    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2]:
            return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    is_spot_empty = False
    for row in board:
        for spot in row:
            if spot == EMPTY:
                is_spot_empty = True

    if is_spot_empty:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    victor = winner(board)
    if victor == X:
        return 1
    elif victor == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            ultimate_value, play = max_value(board)
            return play
        else:
            ultimate_value, play = min_value(board)
            return play


def min_value(board):
    if terminal(board):
        return utility(board), None

    current_value = float('inf')
    play = None
    for action in actions(board):

        # Performing v = min(v, max_value(result(board, action)))
        action_value, action_result = max_value(result(board, action))
        if action_value < current_value:
            current_value = action_value
            play = action
            if current_value == -1:
                return current_value, play

    return current_value, play


def max_value(board):
    if terminal(board):
        return utility(board), None

    current_value = float('-inf')
    play = None
    for action in actions(board):

        # Performing v = min(v, max_value(result(board, action)))
        action_value, action_result = min_value(result(board, action))
        if action_value > current_value:
            current_value = action_value
            play = action
            if current_value == 1:
                return current_value, play

    return current_value, play
