# https://leetcode.com/problems/sudoku-solver/
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# 1. Each of the digits 1-9 must occur exactly once in each row.
# 2. Each of the digits 1-9 must occur exactly once in each column.
# 3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.


# Solution - backtracking
# O(9!^9) time complexity - number of rows, columns and possible values combined
# O(9*3 + 81) space complexity - box, rows, columns sets stored + call stack
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # initialization and setup
        board_size = len(board)
        # initialize lists with sets to remember numbers in each box, row, column
        boxes = []
        rows = []
        cols = []

        for i in range(board_size):
            boxes.append(set())
            rows.append(set())
            cols.append(set())

        # add initial board numbers
        for r in range(board_size):
            for c in range(board_size):
                if board[r][c] != ".":
                    number = board[r][c]
                    # get box id
                    box_id = self.get_box_id(r, c)
                    # add to boxes
                    boxes[box_id].add(number)
                    # add to rows
                    rows[r].add(number)
                    # add to columns
                    cols[c].add(number)

        # Backtracking -------------------------------------------------------------------------------------------------
        self.backtrack(board, boxes, rows, cols, 0, 0)

    #  Helper methods --------------------------------------------------------------------------------------------------
    def get_box_id(self, row, col):
        row_num = (row // 3) * 3
        col_num = col // 3
        # calculates the square 3x3 box inside which is the current cell
        square_id = col_num + row_num

        return square_id

    def contains(self, box, row, col, num):
        # Checks whether number is already contained in the current box, row or column
        if num in box or num in row or num in col:
            return True
        return False

    def backtrack(self, board, boxes, rows, cols, curr_row, curr_col):
        if curr_row >= len(board) or curr_col >= len(board[0]):
            return True
        else:
            if board[curr_row][curr_col] == ".":
                # if the cell is empty, try to fill all of the numbers one by one
                # (1 - 9 included => 1, 10)
                for i in range(1, 10):
                    # add number to the board
                    board[curr_row][curr_col] = str(i)

                    box_id = self.get_box_id(curr_row, curr_col)
                    box = boxes[box_id]
                    row = rows[curr_row]
                    col = cols[curr_col]

                    # check whether the added number already exists in box, row or column
                    if not self.contains(box, row, col, str(i)):
                        box.add(str(i))
                        row.add(str(i))
                        col.add(str(i))
                        # if you get to the end of the current row,
                        # continue from the start of the next row
                        if curr_col >= len(board[0]) - 1:
                            if self.backtrack(board, boxes, rows, cols, curr_row + 1, 0):
                                return True
                        else:
                            # otherwise continue with the next column
                            if self.backtrack(board, boxes, rows, cols, curr_row, curr_col + 1):
                                return True

                        # if the number is already on the board in the current box, row or column
                        box.remove(str(i))
                        row.remove(str(i))
                        col.remove(str(i))

                    # remove the number from the board
                    board[curr_row][curr_col] = "."
            else:
                # if the current cell is already filled, move to the next one
                if curr_col >= len(board[0]) - 1:
                    if self.backtrack(board, boxes, rows, cols, curr_row + 1, 0):
                        return True
                elif self.backtrack(board, boxes, rows, cols, curr_row, curr_col + 1):
                    return True

        return False


solution = Solution()
sudoku_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solution.solveSudoku(sudoku_board)
for row in sudoku_board:
    print(row)
