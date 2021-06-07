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


# Solution 2 - Topological sort
# On(n^2) time complexity, O(n^2) space complexity
class Solution2(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # build an adjacency list --------------------------------------------------------------------------------------
        adjacency = [[] for x in range(numCourses)]

        for vertex in prerequisites:
            adjacency[vertex[1]].append(vertex[0])

        # build indegree list ------------------------------------------------------------------------------------------
        indegree = [0 for _ in range(numCourses)]

        # count number of directions pointing at each vertex - indegree value
        for connection in prerequisites:
            vertex = connection[0]
            indegree[vertex] += 1

        # topological sort - DAG(Directed Acyclic Graph) ---------------------------------------------------------------
        # look for vertex with 0 connections - 0 pointers pointing at it - indegree value 0
        indegree_len = len(indegree) - 1
        stack = []

        # fill stack
        for i in range(len(indegree)):
            if indegree[i] == 0:
                stack.append(i)

        while len(stack) > 0:
            current = stack.pop()
            connected_vertices = adjacency[current]

            # iterate over all connected vertices,
            for connection in connected_vertices:
                # reduce number of connections of vertices the removed vertex is pointing to in indegree list
                indegree[connection] -= 1
                # reduce indegree_len with every processed/removed vertex
                indegree_len -= 1
                # if connection became 0, append it to the stack
                if indegree[connection] == 0:
                    stack.append(connection)

        # check whether all connections from indegree list were removed
        if indegree_len > 0:
            return False
        return True


# solution = Solution()
# print(solution.canFinish(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))
# print(solution.canFinish(2, [[1, 0], [0, 1]]))
# print(solution.canFinish(2, [[1, 0]]))

solution2 = Solution2()
print(solution2.canFinish(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))
print(solution2.canFinish(2, [[1, 0], [0, 1]]))
print(solution2.canFinish(2, [[1, 0]]))
