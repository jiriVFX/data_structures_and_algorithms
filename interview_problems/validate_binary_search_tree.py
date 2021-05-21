# https://leetcode.com/problems/validate-binary-search-tree/
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1 - recursive DFS
# O(n) time complexity, O(n) space complexity
class Solution(object):
    # Using Depth First Search to go through the tree and validate
    def isValidBST(self, root):
        """
        :type root: list
        :rtype: bool
        """
        # Older versions of Python don't have math.inf module, we have to use float("inf") instead
        return self.traverse_preorder(root, -float("inf"), float("inf"))

    # Pre-order DFS traverse
    def traverse_preorder(self, current_node, min_val, max_val):
        # if the current node value is smaller than or equal to minimum, it is not valid BST
        # if the current node value is larger or equal to maximum, it is not a valid BST
        if current_node.val <= min_val or current_node.val >= max_val:
            return False
        # go to the left node, left node's value must be smaller than current node's value
        if current_node.left is not None:
            if not self.traverse_preorder(current_node.left, min_val, current_node.val):
                return False
        # got to the right node, right node's value must be larger than current node's value
        if current_node.right is not None:
            if not self.traverse_preorder(current_node.right, current_node.val, max_val):
                return False

        # If we've got here, it must be a valid BST
        return True
