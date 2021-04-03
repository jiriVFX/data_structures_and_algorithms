# Binary search tree - usually O(log n), but can be O(n) if very unbalanced (becomes just a linked list)

# Collections import so we don't write our own queue methods again (deque.popleft() is approximately O(1))
import collections


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if new_node.value > current_node.value:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        break
                else:
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        break

    # Returns True if the value exists in the tree and False if it doesn't
    # Binary search O(log n)
    def lookup(self, value):
        if self.root is None:
            return False
        current_node = self.root

        while current_node is not None:
            if value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left
            elif value == current_node.value:
                return True
        return False

    # BFS - O(n) time complexity - every node has to be visited
    # O(n) space complexity - in the worst case every node has to be in the queue
    def breadth_first_search(self):
        current_node = self.root
        # using collections.deque() function, so we don't have to write our own here
        queue = collections.deque([])
        print_list = []
        # Start with the first node (root)
        queue.append(current_node)

        while len(queue) > 0:
            # Remove the first node from the queue
            current_node = queue.popleft()
            # Add node value to the print_list
            print_list.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return print_list

    def bfs_recursive(self, queue, print_list):
        # queue argument passed to the method must have already self.root in it
        if len(queue) > 0:
            # Remove the first node from the queue
            current_node = queue.popleft()
            # Add node value to the print_list
            print_list.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
            return self.bfs_recursive(queue, print_list)
        return print_list

    # DFS - O(n) time complexity - every node has to be visited
    # O(height-of-the-tree) space complexity - every node in the current branch is added to stack
    # Pre-order DFS traverse wrapping method
    def depth_first_search_preorder(self):
        return self.traverse_preorder(self.root, [])

    # In-order DFS traverse wrapping method
    def depth_first_search_inorder(self):
        return self.traverse_inorder(self.root, [])

    # Post-order DFS traverse wrapping method
    def depth_first_search_postorder(self):
        return self.traverse_postorder(self.root, [])

    # Pre-order DFS traverse
    def traverse_preorder(self, current_node, print_list):
        print_list.append(current_node.value)
        if current_node.left is not None:
            self.traverse_preorder(current_node.left, print_list)
        if current_node.right is not None:
            self.traverse_preorder(current_node.right, print_list)
        return print_list

    # In-order DFS traverse
    def traverse_inorder(self, current_node, print_list):
        if current_node.left is not None:
            self.traverse_inorder(current_node.left, print_list)
        print_list.append(current_node.value)
        if current_node.right is not None:
            self.traverse_inorder(current_node.right, print_list)
        return print_list

    # Post-order DFS traverse
    def traverse_postorder(self, current_node, print_list):
        if current_node.left is not None:
            self.traverse_postorder(current_node.left, print_list)
        if current_node.right is not None:
            self.traverse_postorder(current_node.right, print_list)
        print_list.append(current_node.value)
        return print_list

        # # Not Working
        # def remove(self, value):
        #     # Search for the node with the value
        #     # If the node is a leaf, delete the node
        #     # If the node has a child, replace the node with the child
        #     # If the node has more children, replace the node with the child on the right (with larger value)
        #     if self.root is None:
        #         return False
        #     current_node = self.root
        #
        #     parent_node = None
        #     while current_node is not None:
        #         if value > current_node.value:
        #             parent_node = current_node
        #             current_node = current_node.right
        #         elif value < current_node.value:
        #             parent_node = current_node
        #             current_node = current_node.left
        #         elif value == current_node.value:
        #             # This is the node we are looking for
        #             if current_node.right is None:
        #                 # If current node has no child on the right
        #                 if parent_node is None:
        #                     # If parent_node is still None, the current_node must be root node
        #                     self.root = current_node.left
        #                 else:
        #                     if current_node.value > parent_node.value:
        #                         # Make the child of the current_node (to be removed) the child of the parent_node
        #                         # So parent node will be pointing on the child of the current_node
        #                         parent_node.right = current_node.left
        #                     elif current_node.value < parent_node.value:
        #                         parent_node.left = current_node.left
        #
        #             elif current_node.left is None:
        #                 # If parent_node is still None, the current_node must be root node
        #                 if parent_node is None:
        #                     # If parent_node is still None, the current_node must be root node
        #                     self.root = current_node.right
        #                 else:
        #                     if current_node.value > parent_node.value:
        #                         # Make the child of the current_node (to be removed) the child of the parent_node
        #                         # So parent node will be pointing on the child of the current_node
        #                         parent_node.right = current_node.right
        #                     elif current_node.value < parent_node.value:
        #                         parent_node.left = current_node.right
        # # If the node has not been found, return False
        # return False


binary_search_tree = BinaryTree()

binary_search_tree.insert(9)
binary_search_tree.insert(4)
binary_search_tree.insert(20)
binary_search_tree.insert(1)
binary_search_tree.insert(6)
binary_search_tree.insert(15)
binary_search_tree.insert(170)

# print(binary_search_tree.lookup(170))

# Calling Breadth First Search method
# print(binary_search_tree.breadth_first_search())
# Calling the recursive BFS method
# new_queue = collections.deque([binary_search_tree.root])
# print(binary_search_tree.bfs_recursive(new_queue, print_list=[]))

# Calling Pre-order Depth First Search method
print(binary_search_tree.depth_first_search_preorder())
# Calling In-order Depth First Search method
print(binary_search_tree.depth_first_search_inorder())
# Calling Post-order Depth First Search method
print(binary_search_tree.depth_first_search_postorder())
