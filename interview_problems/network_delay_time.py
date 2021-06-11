# https://leetcode.com/problems/network-delay-time/
# You are given a network of n nodes, labeled from 1 to n.
# You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node,
# and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k.
# Return the time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.

# Does not work on LeetCode - Time Limit Exceeded
# # MinHeap -------------------------------------------------------------------------------------------------------
# class MinHeap:
#     def __init__(self, heap_list=[]):
#         self.heap_list = heap_list
#
#     def print(self):
#         print(self.heap_list)
#
#     def peek(self):
#         if len(self.heap_list) > 0:
#             return self.heap_list[0]
#         else:
#             return None
#
#     def is_empty(self):
#         if len(self.heap_list) == 0:
#             return True
#         return False
#
#     def length(self):
#         return len(self.heap_list)
#
#     def swap(self, a, b):
#         temp = self.heap_list[a]
#         self.heap_list[a] = self.heap_list[b]
#         self.heap_list[b] = temp
#
#     def pop(self):
#         if len(self.heap_list) > 0:
#             # store popped item to return it at the end
#             popped = self.heap_list[0]
#
#             if len(self.heap_list) > 1:
#                 # swap the first and the last elements
#                 self.heap_list[0] = self.heap_list[-1]
#             # remove the last element
#             self.heap_list.pop()
#             # sift to make sure root is the largest value
#             self.sift_down()
#
#             return popped
#
#     def add(self, item):
#         self.heap_list.append(item)
#         self.sift_up()
#
#     def sift_up(self):
#         i = len(self.heap_list) - 1
#
#         while True:
#             parent = (i - 1) // 2
#
#             if parent < 0:
#                 break
#             # check whether child's value is larger than its parent's value
#             # swap the child and the parent until reaching beginning of the list
#             if self.heap_list[i] > self.heap_list[parent]:
#                 self.swap(parent, i)
#                 # continue from parents position and skip other nodes
#                 i = parent
#             else:
#                 break
#
#     def sift_down(self):
#         i = 0
#
#         while i < len(self.heap_list) - 1:
#             left_child = (i * 2) + 1
#             right_child = (i * 2) + 2
#
#             if left_child >= len(self.heap_list):
#                 break
#
#             # choose the child with the larger value
#             # check whether its value is larger than its parent's value
#             # swap the child and the parent until reaching end of the list
#             if right_child < len(self.heap_list) and self.heap_list[right_child] > self.heap_list[left_child]:
#                 if self.heap_list[i] < self.heap_list[right_child]:
#                     self.swap(i, right_child)
#                     # move pointer to original left child position
#                     i = right_child
#                 else:
#                     break
#             else:
#                 if self.heap_list[i] < self.heap_list[left_child]:
#                     self.swap(i, left_child)
#                     # move pointer to original right child position
#                     i = left_child
#
#
# class Solution(object):
#     def networkDelayTime(self, times, n, k):
#         """
#         :type times: List[List[int]]
#         :type n: int
#         :type k: int
#         :rtype: int
#         """
#         # create shortest path list -------------------------------------------------------------------------
#         # would be math.inf in Python 3 instead of float("inf")
#         # list is +1 in length as vertices start from 1, we don't use 0
#         shortest = [float("inf") for _ in range(n + 1)]
#         shortest[k] = 0
#
#         # create adjacency list ------------------------------------------------------------------------------
#         adjacency = [[] for x in range(n + 1)]
#
#         for vertex in times:
#             adjacency[vertex[0]].append([vertex[1], vertex[2]])
#
#         # print(adjacency)
#
#         # priority queue - min heap ---------------------------------------------------------------------------
#         min_heap = MinHeap()
#         # add the signal node to the min
#         min_heap.add(k)
#
#         # start counting distances -----------------------------------------------------------------------------
#         while not min_heap.is_empty():
#             current = min_heap.pop()
#             connections = adjacency[current]
#
#             # iterate over connected vertices
#             for i in range(len(connections)):
#
#                 vertex = connections[i][0]
#                 distance = connections[i][1]
#                 # if the distance from the current vertex is smaller than the distance of any of its connections
#                 # replace the smallest distance in the shortest list
#                 if shortest[current] + distance < shortest[vertex]:
#                     shortest[vertex] = shortest[current] + distance
#
#                     # add vertex to the heap
#                     min_heap.add(vertex)
#         # get the maximum from shortest list -------------------------------------------------------------------
#         # find maximum distance in shortest except position 0, which we have not used
#         maximum = max(shortest[1:])
#         # if maximum is infinity, it means all vertices can't be reached(at least one vertex is disconnected)
#         if maximum == float("inf"):
#             return -1
#         else:
#             return maximum


# Using built in python heap queue
import heapq


# Dijkstra's algorithm
# O(E log n) time complexity
# O(E + n) space complexity
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # create shortest path list ----------------------------------------------------------------------------
        # would be math.inf in Python 3 instead of float("inf")
        # list is +1 in length as vertices start from 1, we don't use 0
        shortest = [float("inf") for _ in range(n + 1)]
        shortest[k] = 0

        # create adjacency list --------------------------------------------------------------------------------
        adjacency = [[] for x in range(n + 1)]

        for vertex in times:
            adjacency[vertex[0]].append([vertex[1], vertex[2]])

        # priority queue - min heap ----------------------------------------------------------------------------
        # min_heap = MinHeap()
        heap_list = [k]
        # add the signal node to the min
        heapq.heapify(heap_list)

        # start counting distances -----------------------------------------------------------------------------
        while len(heap_list) > 0:
            # while not min_heap.is_empty():
            # current = min_heap.pop()
            current = heapq.heappop(heap_list)
            connections = adjacency[current]

            # iterate over connected vertices
            for i in range(len(connections)):
                vertex = connections[i][0]
                distance = connections[i][1]
                # if the distance from the current vertex is smaller than the distance of any of its connections
                # replace the smallest distance in the shortest list
                if shortest[current] + distance < shortest[vertex]:
                    shortest[vertex] = shortest[current] + distance
                    # add vertex to the heap
                    # min_heap.add(vertex)
                    heapq.heappush(heap_list, vertex)

        # get the maximum from shortest list -------------------------------------------------------------------
        # find maximum distance in shortest except position 0, which we have not used
        maximum = max(shortest[1:])
        # if maximum is infinity, it means all vertices can't be reached(at least one vertex is disconnected)
        if maximum == float("inf"):
            return -1
        else:
            return maximum


# Bellman-Ford algorithm
# O(n * e) time complexity
# O(n) space complexity
class Solution2(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # create shortest path list ----------------------------------------------------------------------------
        # would be math.inf in Python 3 instead of float("inf")
        # list is +1 in length as vertices start from 1, we don't use 0
        distances = [float("inf") for _ in range(n + 1)]
        distances[k] = 0

        # Bellman-Ford algorithm -------------------------------------------------------------------------------
        # Much easier to implement compared Dijkstra's
        # we just need distances list to store the shortest distance to each node found
        for i in range(n):
            # check every connection distance against distance in distances list
            # if shorter distance is found, replace the corresponding value in distances list
            changed = False
            for j in range(len(times)):
                start_vertex = times[j][0]
                dest_vertex = times[j][1]
                current_distance = times[j][2]
                if distances[dest_vertex] > distances[start_vertex] + current_distance:
                    changed = True
                    distances[dest_vertex] = distances[start_vertex] + current_distance

            # if no distance was changed, quit iterating to save time
            if not changed:
                break

        # get the maximum from shortest list -------------------------------------------------------------------
        # find maximum distance in shortest except position 0, which we have not used
        maximum = max(distances[1:])
        # if maximum is infinity, it means all vertices can't be reached(at least one vertex is disconnected)
        if maximum == float("inf"):
            return -1
        else:
            return maximum


print("Dijkstra's algorithm:")
dijkstra = Solution()
print(dijkstra.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(dijkstra.networkDelayTime(
    [[3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85], [5, 2, 22], [2, 4, 23], [1, 4, 43], [4, 5, 75],
     [5, 1, 15], [1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31], [1, 2, 0], [2, 5, 4], [4, 2, 51],
     [3, 1, 36], [2, 3, 59]], 5, 5, ))

print("\nBellman-Ford algorithm:")
bellman_ford = Solution2()
print(bellman_ford.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(bellman_ford.networkDelayTime(
    [[3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85], [5, 2, 22], [2, 4, 23], [1, 4, 43], [4, 5, 75],
     [5, 1, 15], [1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31], [1, 2, 0], [2, 5, 4], [4, 2, 51],
     [3, 1, 36], [2, 3, 59]], 5, 5, ))
