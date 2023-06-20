from tictactoe import winner

X = "X"
O = "O"
EMPTY = None

board = [[O, X, X],
            [O, O, X],
            [EMPTY, O, O]]
print(winner(board))

