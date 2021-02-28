# # Graph
#
# # Edge List
# graph_using_edge_list = [[0, 2], [2, 3], [2, 1], [1, 3]]
#
# # Adjacency List - contains only connections of the current index
# # Connections of node 2 would be accessed by graph_with_adjacent_list[1] that is [2, 3]
# graph_using_adjacent_list = [[2], [2, 3], [1, 2, 3], [1, 2]]
#
# # Adjacent matrix - 0s and 1s
# # 0 when there is no connection to the node, 1 when there is a connection
# # As an two-dimensional array
# graph_using_adjacent_matrix = [
#     [0, 0, 1, 0], # Index 0 is connected to node 2
#     [0, 0, 1, 1], # Index 1 is connected to nodes 2, 3
#     [1, 1, 0, 1], # Index 2 is connected to nodes 0, 1 and 3
#     [0, 1, 1, 0]  # Index 3 is connected to nodes 1 and 2
# ]
# # As a dictionary
# graph_using_adjacent_dictionary = {
#    "A": [0, 0, 1, 0], # Index 0 is connected to node 2
#    "B": [0, 0, 1, 1], # Index 1 is connected to nodes 2, 3
#    "C": [1, 1, 0, 1], # Index 2 is connected to nodes 0, 1 and 3
#    "D": [0, 1, 1, 0]  # Index 3 is connected to nodes 1 and 2
# }


# Undirected unweighted graph using adjacency list
# Dictionary(Hash table) used for the adjacency list
class Graph:
    def __init__(self):
        self.adjacent_list = {}

    def add_vertex(self, vertex_value):
        self.adjacent_list[vertex_value] = []

    def add_edge(self, vertex1, vertex2):
        # Undirected graph
        # All vertices have a list with their connections
        self.adjacent_list[vertex1].append(vertex2)
        self.adjacent_list[vertex2].append(vertex1)

    def print_adjacent_list(self):
        print(self.adjacent_list)
    # def show_connections()


my_graph = Graph()
my_graph.add_vertex('0')
my_graph.add_vertex('1')
my_graph.add_vertex('2')
my_graph.add_vertex('3')
my_graph.add_vertex('4')
my_graph.add_vertex('5')
my_graph.add_vertex('6')
my_graph.add_edge('3', '1')
my_graph.add_edge('3', '4')
my_graph.add_edge('4', '2')
my_graph.add_edge('4', '5')
my_graph.add_edge('1', '2')
my_graph.add_edge('1', '0')
my_graph.add_edge('0', '2')
my_graph.add_edge('6', '5')

my_graph.print_adjacent_list()
