from collections import deque


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    # O(v + e) time complexity (every node and every edge is visited)
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

    #  O(v + e) time complexity (every node and every edge is visited)
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
                # we have to traverse the adjacency list from the end or reverse it
                # so the first connected vertex is the last added to the stack
                # in the next iteration, the first vertex from the adjacency list will be popped
                # this is necessary, otherwise the returned values list is in different order
                # compared to the one returned by the recursive method
                for vertex in reversed(self.adjacency_list[current]):
                    # add all connected vertices,
                    # but only if they were not visited yet
                    if vertex not in seen:
                        # add to a stack
                        stack.append(vertex)

        return values

    # O(v + e) time complexity (every node and every edge is visited)
    # O(n) space complexity
    # main driving method
    def dfs_traversal_recursive(self, start):
        if len(self.adjacency_list) > 0:
            values = []
            seen = set()
            return self.dfs_recursive(start, values, seen)

    # recursive traversal method
    def dfs_recursive(self, vertex, values, seen):
        # append actual vertex value to return at the end
        values.append(vertex)
        # remember visited vertices
        seen.add(vertex)

        for connected_vertex in self.adjacency_list[vertex]:
            # call itself on every not visited connected vertex
            if connected_vertex not in seen:
                self.dfs_recursive(connected_vertex, values, seen)

        return values


list_of_connections = [[1, 3], [0], [3, 8], [0, 2, 4, 5], [3, 6], [3], [4, 7], [6], [2]]
graph = Graph(list_of_connections)
print(f"Graph BFS:     {graph.bfs_traversal(0)}")
print(f"Graph DFS:     {graph.dfs_traversal(0)}")
print(f"Recursive DFS: {graph.dfs_traversal_recursive(0)}")
