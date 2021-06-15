# https://leetcode.com/problems/knight-probability-in-chessboard/
# On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves.
# The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
# A chess knight has eight possible moves it can make, as illustrated below.
# Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.
# Each time the knight is to move, it chooses one of eight possible moves uniformly at random
# (even if the piece would go off the chessboard) and moves there.
# The knight continues moving until it has made exactly k moves or has moved off the chessboard.
# Return the probability that the knight remains on the board after it has stopped moving.


def knightProbability(n, k, row, column):
    """
    :type n: int
    :type k: int
    :type row: int
    :type column: int
    :rtype: float
    """
    if k == 0:
        return 1

    knight_r = row
    knight_c = column

    # create a list of all possible knight moves
    moves = [
        [2, -1],
        [2, 1],
        [-2, -1],
        [-2, 1],
        [1, -2],
        [1, 2],
        [-1, -2],
        [-1, 2]
    ]

    # Initialize position lists to hold moves probability
    positions = []

    # k + 1 number of tables
    for i in range(k + 1):
        positions.append([])
        # rows
        for j in range(n):
            positions[i].append([])
            # columns
            for l in range(n):
                positions[i][j].append(0.0)

    # set the starting position probability
    # be careful to initialize all values as float in Python 2.x - not necessary in Python 3.x
    positions[0][row][column] = 1.0
    print(positions)
    # do k number of moves ----------------------------------------------------------------------------------------
    for step in range(1, k + 1):
        for r in range(n):
            for c in range(n):
                # test every possible move from current position
                for move in moves:
                    # move is inside chessboard
                    knight_r = r + move[0]
                    knight_c = c + move[1]

                    if knight_r >= n or knight_r < 0 or knight_c >= n or knight_c < 0:
                        # move is out of chessboard
                        pass
                    else:
                        # add probability in positions (divided by 8 - number of all possible moves)
                        positions[step][r][c] += positions[step - 1][knight_r][knight_c] / 8

    # return result -------------------------------------------------------------------------------------------------
    probability = 0.0

    # make a sum of all probabilities
    for r in range(n):
        for c in range(n):
            probability += positions[k][r][c]

    return probability


print(knightProbability(n=3, k=2, row=0, column=0))
print(knightProbability(n=1, k=0, row=0, column=0))
