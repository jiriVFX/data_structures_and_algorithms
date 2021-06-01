from collections import deque


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    # O(n) time complexity
    # O(n) space complexity
    def bfs_traversal(self, start):
        if len(self.adjacency_list) > 0:
            queue = deque([start])
            values = []
            seen = set()

        while len(queue) > 0:
            current = queue.popleft()
            # append actual vertex value to return at the end
            values.append(current)
            # remember visited vertices
            seen.add(current)

            # check adjacency list for connections
            if len(self.adjacency_list[current]) > 0:
                for vertex in self.adjacency_list[current]:
                    # add all connected vertices,
                    # but only if they were not visited yet
                    if vertex not in seen:
                        queue.append(vertex)

        return values

    # O(n) time complexity
    # O(n) space complexity
    def dfs_traversal(self, start):
        if len(self.adjacency_list) > 0:
            stack = [start]
            values = []
            seen = set()

        while len(stack) > 0:
            current = stack.pop()
            if current not in seen:
                # append actual vertex value to return at the end
                values.append(current)
                # remember visited vertices
                seen.add(current)

            # check adjacency list for connections
            if len(self.adjacency_list[current]) > 0:
                for vertex in self.adjacency_list[current]:
                    # add all connected vertices,
                    # but only if they were not visited yet
                    if vertex not in seen:
                        # add to a stack
                        stack.append(vertex)

        return values


list_of_connections = [[1, 3], [0], [3, 8], [0, 2, 4, 5], [3, 6], [3], [4, 7], [6], [2]]
graph = Graph(list_of_connections)
print(graph.bfs_traversal(0))
print(graph.dfs_traversal(0))
