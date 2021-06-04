# https://leetcode.com/problems/course-schedule/
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
# that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.


from collections import deque


# Solution 1 - BFS for every single vertex (inefficient)
# O(n^3) time complexity, O(n^2) space complexity
class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # if there is a cycle in a graph return False

        # build an adjacency list --------------------------------------------------------------------------------------
        adjacency = [[] for x in range(numCourses)]

        for vertex in prerequisites:
            adjacency[vertex[1]].append(vertex[0])

        # BFS traversal ------------------------------------------------------------------------------------------------
        # start BFS from every single vertex in case all vertices are not connected
        for i in range(len(adjacency)):
            if len(adjacency[i]) > 0:
                if not self.bfs_traversal(adjacency, i):
                    return False
        return True

    # BFS method
    def bfs_traversal(self, adjacency, start):
        if len(adjacency) > 0:
            queue = deque([])
            traversed = 0
            seen = set()

        # add all vertices in adjacency list to the queue
        for vertex in adjacency[start]:
            queue.append(vertex)

        while len(queue) > 0:
            current = queue.popleft()
            # count visited vertices
            traversed += 1

            # if the starting vertex is in the queue (pointing at itself), there is a loop
            if current == start:
                return False

            # check adjacency list for connections
            if len(adjacency[current]) > 0:
                for vertex in adjacency[current]:
                    # add all connected vertices,
                    # but only if they were not visited yet
                    if vertex not in seen:
                        queue.append(vertex)
                        seen.add(vertex)
        return True


solution = Solution()
print(solution.canFinish(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))
print(solution.canFinish(2, [[1, 0], [0, 1]]))
print(solution.canFinish(2, [[1, 0]]))
