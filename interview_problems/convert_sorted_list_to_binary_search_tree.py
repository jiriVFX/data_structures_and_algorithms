# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Given the head of a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1 - top-down approach - recursion with fast and slow pointer
# O(n log n) time complexity, O(1) space complexity
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # find the middle of the list and start from there
        # The middle node becomes the root and the list is split in left and right side
        # this is done until the safety check below is not passed => whole tree is constructed

        # Safety check
        if head is None:
            return head
        if head.next is None:
            return TreeNode(val=head.val)
        # --------------------------------------------------------------------------------------------------------------

        # get the middle node
        middle = self.find_middle(head)
        # print(middle.val)

        # create tree node
        tree_node = TreeNode(val=middle.val)

        # Go through the left and the right side
        tree_node.left = self.sortedListToBST(head)
        tree_node.right = self.sortedListToBST(middle.next)

        return tree_node

        # --------------------------------------------------------------------------------------------------------------

    # Helper method to find the middle node
    def find_middle(self, head):
        fast = head
        slow = head
        pre_slow = None

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            pre_slow = slow
            slow = slow.next

        # Break the left side connection to the right side of the current list
        # the list now spreads from the head to one the node before slow
        pre_slow.next = None

        return slow
