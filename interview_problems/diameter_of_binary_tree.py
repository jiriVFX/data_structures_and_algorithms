# https://leetcode.com/problems/diameter-of-binary-tree/
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1 - Depth-First-Search recursive
# O(n) time complexity, O(n) space complexity
# We are looking for the longest path from one node to another
# We need to calculate height of the left subtree and the right sub tree
# and add both heights and root node to get the longest path
class Solution(object):
    def __init__(self):
        # if the binary tree has at least root, the depth is already 1
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        # call the maximum_depth_dfs on the tree root
        self.maximum_depth_dfs(root)

        return self.max_diameter

    # DFS helper method
    def maximum_depth_dfs(self, root):
        # Failsafe
        if root is None:
            return 0

        max_depth_left = self.maximum_depth_dfs(root.left)
        max_depth_right = self.maximum_depth_dfs(root.right)
        # choose new max - the larger between max_diameter and the current subtree
        self.max_diameter = max(self.max_diameter, max_depth_left + max_depth_right)

        # increment depth by one
        return max(max_depth_left, max_depth_right) + 1
