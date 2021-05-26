# https://leetcode.com/problems/number-of-islands/
# Given an m x n 2D binary grid "grid" which represents a map of '1's (land) and '0's (water),
# return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

from collections import deque


# Breadth-First-Search Solution
# O(n) time complexity or O(m * n) - every field should be visited only once
# O(n) space complexity or O(m * n - the matrix diagonal)
class Solution(object):
    def __init__(self):
        self.queue = deque([])

    def num_islands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    islands += self.bfs_islands(grid, (r, c))
        return islands

    # Breadth-First-Search for islands
    def bfs_islands(self, grid, position):
        # add position to the queue
        self.queue.append(position)

        while len(self.queue) > 0:
            current = self.queue.popleft()

            # Had to add a "hotfix" to check if the current position is not "0", due to an undiscovered bug,
            # when nodes get added to the queue even when they are not "1"
            if grid[current[0]][current[1]] == "0":
                continue

            # change current position to "0" to mark as visited
            grid[current[0]][current[1]] = "0"

            # check left
            if (current[1] - 1 >= 0) and (grid[current[0]][current[1] - 1] == "1"):
                self.queue.append((current[0], current[1] - 1))
            # check right
            if (current[1] + 1 < len(grid[0])) and (grid[current[0]][current[1] + 1] == "1"):
                self.queue.append((current[0], current[1] + 1))
            # check top
            if (current[0] - 1 >= 0) and (grid[current[0] - 1][current[1]] == "1"):
                self.queue.append((current[0] - 1, current[1]))
            # check bottom
            if (current[0] + 1 < len(grid)) and (grid[current[0] + 1][current[1]] == "1"):
                self.queue.append((current[0] + 1, current[1]))
        return 1


island_counter = Solution()
print(island_counter.num_islands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(island_counter.num_islands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
print(island_counter.num_islands([
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "1", "1"]
]))
print(island_counter.num_islands([["1", "1"]]))
print(island_counter.num_islands([
    ["1"],
    ["1"]
]))
print(island_counter.num_islands([
    ["1", "0", "1", "1", "0", "1", "1"]
]))
print(island_counter.num_islands([
    ["1", "0", "1", "1", "1"],
    ["1", "0", "1", "0", "1"],
    ["1", "1", "1", "0", "1"]
]))
print(island_counter.num_islands([
    ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1"],
    ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0"],
    ["1", "0", "1", "1", "1", "0", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1"],
    ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
]))
