# https://leetcode.com/problems/symmetric-tree/
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive
# O(n) time complexity (checking each node)
# O(h) space complexity (height of the tree - we are going from the root down to the last leaf and back up)
class Solution(object):
    def is_symmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check_branches(root.left, root.right)

    def check_branches(self, left_branch, right_branch):
        # If both are None, we are at the bottom of the tree
        if left_branch is None and right_branch is None:
            return True
        # Otherwise check values and go recursively through each node's subtrees
        elif left_branch is not None and right_branch is not None:
            return left_branch.val == right_branch.val and self.check_branches(left_branch.left, right_branch.right) \
                   and self.check_branches(left_branch.right, right_branch.left)
        # If right doesn't equal left, then the tree is not a mirror of itself
        return False


# Iterative - BFS using queue
# O(n) time complexity (checking each node)
# O(h) space complexity (height of the tree - we are going from the root down to the last leaf and back up)
import collections


class Solution2(object):
    def is_symmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = collections.deque([])
        queue.append(root.left)
        queue.append(root.right)

        while len(queue) > 0:
            branch_left = queue.popleft()
            branch_right = queue.popleft()

            if branch_left is None and branch_right is None:
                # Does not mean we are at the end as long as there are other nodes in the queue
                # Make sure it won't be an infinite loop
                # Skip all queue.append, because child of None is always None
                continue
            elif branch_left is None or branch_right is None:
                # If only one is None, they are not the same
                return False
            elif branch_left is not None and branch_right is not None:
                if branch_left.val != branch_right.val:
                    return False

            queue.append(branch_left.left)
            queue.append(branch_right.right)
            queue.append(branch_left.right)
            queue.append(branch_right.left)
        return True
