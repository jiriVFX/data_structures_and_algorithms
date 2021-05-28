# https://www.lintcode.com/problem/663/
# You are given a m x n 2D grid initialized with these three possible values.
# -1 - A wall or an obstacle. 0 - A gate. INF - Infinity means an empty room.
# We use the value 2^31 - 1 = 2147483647 to represent INF
# as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate.
# If it is impossible to reach a Gate, that room should remain filled with INF

# Solution 1 - DFS (iterative)
# O(n) time complexity (number of gates * n)
# O(n) space complexity
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def wallsAndGates(self, rooms):
        gates = []

        # find all the gates
        for row in range(len(rooms)):
            for col in range(len(rooms[row])):
                if rooms[row][col] == 0:
                    self.dfs_distances(rooms, row, col, 0)

    def dfs_distances(self, rooms, row, col, steps):
        # as with the recursive solution, we have to keep track of the steps inside the stack
        stack = [(row, col, steps)]
        directions = (-1, 1)

        while len(stack) > 0:
            current = stack.pop()
            # add one step with every distance level
            steps = current[2] + 1

            # check all sides
            for i in directions:
                # check up and down
                if 0 <= current[0] + i < len(rooms) and rooms[current[0] + i][current[1]] > steps:
                    # replace value with current steps
                    rooms[current[0] + i][current[1]] = steps
                    # add position and current steps to stack
                    stack.append((current[0] + i, current[1], steps))
                # check left and right
                if 0 <= current[1] + i < len(rooms[current[0]]) and rooms[current[0]][current[1] + i] > steps:
                    # replace value with current steps
                    rooms[current[0]][current[1] + i] = steps
                    # add position and current steps to stack
                    stack.append((current[0], current[1] + i, steps))


# ----------------------------------------------------------------------------------------------------------------------

INF = 2147483647
test_1 = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]
solution = Solution()
solution.wallsAndGates(test_1)
for row in test_1:
    print(row)

# Expected result
# [
# [3,-1,0,1],
# [2,2,1,-1],
# [1,-1,2,-1],
# [0,-1,3,4]
# ]
