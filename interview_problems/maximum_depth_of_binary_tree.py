# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Given the root of a binary tree, return its maximum depth.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Until we get to the leaf node
        if root is not None:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            # Return larger depth + root node
            return max(left_depth, right_depth) + 1
        else:
            # When we get recursively to the bottom of the tree, return 0
            # From there go back up node by node with return max(left_depth, right_depth) + 1
            return 0