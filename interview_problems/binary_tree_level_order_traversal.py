# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Given the root of a binary tree,
# return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


# Solution 1 - Breadth First Search
# O(n) time complexity - even though we have nested while loops, every node is accessed only once
# O(n) space complexity
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = deque([])
        queue.append(root)

        levels = []

        # BFS - Breadth First Search
        while len(queue) > 0:
            current_level = []
            level_length = len(queue)
            counter = 0
            # current level consists of nodes, that are already in the queue at this point
            # we have to count how many times we pop the queue
            # to make sure we don't start to iterate over child nodes from the next level (the ones added in this loop)
            while counter < level_length:
                current_node = queue.popleft()
                # append value to the current_level
                current_level.append(current_node.val)

                # add child nodes to the queue
                # we will iterate over the child nodes only in the next iteration of the main loop
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
                # increment counter
                counter += 1

            # append current_level list to levels result list
            levels.append(current_level)

        return levels
