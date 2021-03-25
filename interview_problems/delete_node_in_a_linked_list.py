# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Write a function to delete a node in a singly-linked list.
# You will not be given access to the head of the list,
# instead you will be given access to the node to be deleted directly.
# It is guaranteed that the node to be deleted is not a tail node in the list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # We can't simply change pointers as we have no way to access previous node
        # So we just copy the value of the next node to the current one
        # And at the end of the list we remove the last node
        while node.next.next:
            node.val = node.next.val
            node = node.next
        # Now we have last two nodes and have to remove the pointer to the last node
        node.val = node.next.val
        node.next = None
