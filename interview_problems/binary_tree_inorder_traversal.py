# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Follow up:
# Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1 - recursion
# O(n) time complexity - visiting every node, O(n) space complexity
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Inorder - Left -> Node -> Right
        if root is None:
            return []

        return self.traverse_inorder(root, [])

    def traverse_inorder(self, node, val_list):
        # visit left node
        if node.left is not None:
            self.traverse_inorder(node.left, val_list)
        # visit current node
        val_list.append(node.val)
        # visit right node
        if node.right is not None:
            self.traverse_inorder(node.right, val_list)
        return val_list


# Solution 2 - iterative using our own stack
# O(n) time complexity - visiting every node, O(n) space complexity
class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Inorder - Left -> Node -> Right
        if root is None:
            return []

        val_list = []
        stack = []
        current_node = root

        while current_node is not None or len(stack) > 0:
            # visit all the left nodes
            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.left

            # when there are no more left nodes in the current branch
            current_node = stack.pop()
            val_list.append(current_node.val)

            # visit right node
            # curent_node.right has to be assigned even if it is None
            # otherwise we would get infinite loop visiting left nodes at the beginning
            current_node = current_node.right

        # when the stack is empty, tree was traversed
        return val_list
