# https://leetcode.com/problems/rotting-oranges/
# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1.

from collections import deque


# Solution 1 - BFS
# O(n) time complexity (visiting every node up to two times - 2n)
# O(n) space complexity (queue)
class Solution(object):
    def __init__(self):
        self.minutes = 0
        self.fresh = 0

    def oranges_rotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # reset self variables before running again
        # necessary only when running locally, LeetCode re-initializes objects for each test case
        self.__init__()

        rotten_oranges = []

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # find all rotten oranges
                if grid[row][col] == 2:
                    rotten_oranges.append((row, col))
                # count all fresh oranges
                elif grid[row][col] == 1:
                    self.fresh += 1

        # when all rotten oranges have been found,
        # and there is at least one fresh orange, start BFS
        if self.fresh > 0:
            self.bfs(rotten_oranges, grid)

        # check whether there are any fresh oranges left
        if self.fresh > 0:
            return -1
        return self.minutes

    # Breadth First Search helper method
    # simply looks on each side around current position for fresh oranges
    def bfs(self, rotten_oranges, grid):
        queue = deque(rotten_oranges)
        queue_length = len(queue)
        counter = 0

        while len(queue) > 0:
            # keep track of rounds / levels to count minutes passed
            # every level is a minute
            if counter == queue_length:
                self.minutes += 1
                counter = 0
                queue_length = len(queue)

            current = queue.popleft()
            # we have to rot oranges at the same time as adding them to the queue,
            # otherwise they might be added multiple times

            # check for orange up
            if current[0] - 1 >= 0 and grid[current[0] - 1][current[1]] == 1:
                queue.append((current[0] - 1, current[1]))
                # rot the orange
                grid[current[0] - 1][current[1]] = 2
                self.fresh -= 1
            # check for orange down
            if current[0] + 1 < len(grid) and grid[current[0] + 1][current[1]] == 1:
                queue.append((current[0] + 1, current[1]))
                # rot the orange
                grid[current[0] + 1][current[1]] = 2
                self.fresh -= 1
            # check for orange left
            if current[1] - 1 >= 0 and grid[current[0]][current[1] - 1] == 1:
                queue.append((current[0], current[1] - 1))
                # rot the orange
                grid[current[0]][current[1] - 1] = 2
                self.fresh -= 1
            # check for orange right
            if current[1] + 1 < len(grid[current[0]]) and grid[current[0]][current[1] + 1] == 1:
                queue.append((current[0], current[1] + 1))
                # rot the orange
                grid[current[0]][current[1] + 1] = 2
                self.fresh -= 1

            # increment counter
            counter += 1


solution = Solution()
print(solution.oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(solution.oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(solution.oranges_rotting([[0, 2]]))
print(solution.oranges_rotting([[2, 2], [1, 1], [0, 0], [2, 0]]))
