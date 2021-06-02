# https://leetcode.com/problems/time-needed-to-inform-all-employees/
# A company has n employees with a unique ID for each employee from 0 to n - 1.
# The head of the company is the one with headID.
# Each employee has one direct manager given in the manager array
# where manager[i] is the direct manager of the i-th employee, manager[headID] = -1.
# Also, it is guaranteed that the subordination relationships have a tree structure.
# The head of the company wants to inform all the company employees of an urgent piece of news.
# He will inform his direct subordinates, and they will inform their subordinates,
# and so on until all employees know about the urgent news.
# The i-th employee needs informTime[i] minutes to inform all of his direct subordinates
# (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).
# Return the number of minutes needed to inform all the employees about the urgent news.


# O(vertices + edges) time complexity
# O(n) space complexity
class Solution(object):
    def __init__(self):
        self.adjacency_dict = {}
        self.max_minutes = 0

    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        # Build an adjacency list ---------------------------------------------------------------

        # reset self.max_minutes
        self.max_minutes = 0
        # find out number of managers
        unique_managers = set()
        for i in range(len(manager)):
            if manager[i] != -1:
                unique_managers.add(manager[i])

        # initialize adjacency list with correct length
        self.adjacency_dict = {m: [] for m in unique_managers}

        # fill the adjacency list with managers and their subordinates
        for i in range(len(manager)):
            if manager[i] != -1:
                self.adjacency_dict[manager[i]].append(i)

        # print(self.adjacency_dict)

        # Traverse the graph and count the minutes --------------------------------------------------
        # DFS traversal
        if len(self.adjacency_dict) > 0:
            seen = [False for vertex in range(len(manager))]
            self.dfs_recursive(headID, 0, seen, informTime)
            return self.max_minutes
        else:
            return 0

    # recursive traversal method
    def dfs_recursive(self, vertex, minutes, seen, inform_time):
        # add infromTime to minutes
        self.max_minutes = max(minutes, self.max_minutes)

        # remember visited vertices
        seen[vertex] = True

        # check whether vertex is manager (has any subordinates / children vertices)
        if vertex in self.adjacency_dict:
            connections = self.adjacency_dict[vertex]

            for connection in connections:
                # call itself on every not visited connected vertex
                if not seen[connection]:
                    self.dfs_recursive(connection, minutes + inform_time[vertex], seen, inform_time)

solution = Solution()
print(solution.numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]))
print(solution.numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]))
print(solution.numOfMinutes(n=7, headID=6, manager=[1, 2, 3, 4, 5, 6, -1], informTime=[0, 6, 5, 4, 3, 2, 1]))
print(solution.numOfMinutes(n=15, headID=0, manager=[-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                            informTime=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution.numOfMinutes(n=4, headID=2, manager=[3, 3, -1, 2], informTime=[0, 0, 162, 914]))
