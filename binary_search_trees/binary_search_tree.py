# Binary search tree - usually O(log n), but can be O(n) if very unbalanced (becomes just a linked list)

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
    def lookup(self,value):
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

        # If the node has not been found, return False
        return False



binary_search_tree = BinaryTree()

binary_search_tree.insert(9)
binary_search_tree.insert(4)
binary_search_tree.insert(20)
binary_search_tree.insert(1)
binary_search_tree.insert(6)
binary_search_tree.insert(15)
binary_search_tree.insert(170)

print(binary_search_tree.remove(9))
print(binary_search_tree.lookup(170))
#print(binary_search_tree.print_tree(binary_search_tree.root))

