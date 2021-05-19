# https://leetcode.com/problems/count-complete-tree-nodes/
# Given the root of a complete binary tree, return the number of the nodes in the tree.
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
# and all nodes in the last level are as far left as possible.
# It can have between 1 and 2h nodes inclusive at the last level h.
#
# Design an algorithm that runs in less than O(n) time complexity.


# Solution 1 - binary search
# O(log n * log n) time complexity, O(1) space complexity
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        current_node = root
        height = 0

        # calculate height of the tree ---------------------------------------------------------------------------------

        while current_node.left is not None:
            current_node = current_node.left
            height += 1

        # calculate the number of nodes in all the levels except the very last one -------------------------------------

        # number of the nodes in all the levels expect the last one
        top_level_nodes = 2 ** height - 1

        # possible number of the nodes in the last level
        bottom_nodes = 2 ** (height - 1)

        # calculate number of nodes in the last level ------------------------------------------------------------------
        # now we can conduct binary search on the tree
        # we know max number of the nodes in the last level - bottom_nodes
        left = 0
        right = top_level_nodes

        # binary search
        while left < right:
            # we need to get node in the middle + 1 to the right
            # !!! always divide by 2.0, otherwise numbers inside ceil will be treated as integers !!!
            middle = math.ceil((left + right) / 2.0)
            # go to the middle node
            # if middle is not None, left becomes middle + 1
            # if middle is None, right becomes middlde - 1
            if self.check_node(root, middle, height):
                left = middle
            else:
                right = middle - 1

        # Calculate the final number of all nodes ----------------------------------------------------------------------
        # print(top_level_nodes)
        all_nodes = top_level_nodes + left + 1
        return int(all_nodes)

    # helper method, checks whether node at specified position at the bottom level exists or is None -------------------
    def check_node(self, root, target, height):
        current_level = 0
        left = 0
        right = 2 ** height - 1
        current_node = root

        while current_level < height:
            # we need to get node in the middle + 1 to the right
            # !!! always divide by 2.0, otherwise numbers inside ceil will be treated as integers !!!
            middle = math.ceil((left + right) / 2.0)

            # if target node position is higher than current middle position
            if target >= middle:
                current_node = current_node.right
                left = middle
            else:
                current_node = current_node.left
                right = middle - 1

            # increment level
            current_level += 1

        # at this point we have reached the target position
        # current_node can be either TreeNode or None
        if current_node is None:
            return False
        else:
            return True
