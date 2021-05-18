# https://leetcode.com/problems/binary-tree-right-side-view/
# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


# Solution 1 - BFS
# O(n) time complexity, O(n) space complexity
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        queue = deque([])
        queue.append(root)

        right_values = []

        # We can use BFS
        # we store current level node values in a list
        # at the end of the level we can identify the rightmost item of the level (the last item in the list)
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

            # append the last item from current_level to levels right_values list
            right_values.append(current_level[-1])

        return right_values


# Solution 2 - DFS
# O(n) time complexity, O(n) space complexity
class Solution2(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        # keep the rightmost values in the list
        right_values = []

        # call recursive DFS
        self.dfs_preorder(root, 0, right_values)

        return right_values

    # DFS - Depth First Search - Preorder
    def dfs_preorder(self, current_node, level, right_values):
        # basecase
        if current_node is None:
            return

        # append values only if the current level is higher than any previous one (length of right_values)
        if level >= len(right_values):
            right_values.append(current_node.val)

        # traverse right
        if current_node.right is not None:
            self.dfs_preorder(current_node.right, level + 1, right_values)

        # traverse left
        if current_node.left is not None:
            self.dfs_preorder(current_node.left, level + 1, right_values)
