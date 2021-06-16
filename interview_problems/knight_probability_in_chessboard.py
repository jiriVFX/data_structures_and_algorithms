# https://leetcode.com/problems/knight-probability-in-chessboard/
# On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves.
# The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
# A chess knight has eight possible moves it can make, as illustrated below.
# Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.
# Each time the knight is to move, it chooses one of eight possible moves uniformly at random
# (even if the piece would go off the chessboard) and moves there.
# The knight continues moving until it has made exactly k moves or has moved off the chessboard.
# Return the probability that the knight remains on the board after it has stopped moving.

# Solution one - bottom up approach
# Time complexity - O(k * n^2)
# Space complexity - O(n^2)
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
    positions_prev = [[0.0 for i in range(n)] for j in range(n)]
    positions_next = [[0.0 for i in range(n)] for j in range(n)]

    # set the starting position probability
    # be careful to initialize all values as float in Python 2.x - not necessary in Python 3.x
    positions_prev[row][column] = 1.0

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
                        positions_next[r][c] += positions_prev[knight_r][knight_c] / 8

        # move current positions to positions_prev and initialize positions_next for the next step
        positions_prev = positions_next
        positions_next = [[0.0 for i in range(n)] for j in range(n)]

    # return result -------------------------------------------------------------------------------------------------
    probability = 0.0

    # make a sum of all probabilities
    for r in range(n):
        for c in range(n):
            # only positions_prev has values as positions_next is filled with zeroes
            probability += positions_prev[r][c]

    return probability


print(knightProbability(n=3, k=2, row=0, column=0))
print(knightProbability(n=1, k=0, row=0, column=0))
print(knightProbability(n=8, k=30, row=6, column=4))
