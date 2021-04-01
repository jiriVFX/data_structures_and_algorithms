# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def merge_two_lists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # I any of the lists in empty, return the other list
        if l1 is None or l2 is None:
            if l1 is not None:
                return l1
            if l2 is not None:
                return l2
            # If both lists are empty return None
            return None

        # Otherwise continue with merging the lists
        # assign the first (head) node to the sorted_list
        if l1.val < l2.val:
            sorted_head = l1
            l1 = l1.next
        else:
            sorted_head = l2
            l2 = l2.next

        sorted_current = sorted_head

        # Merge the lists until the last node
        while l1 or l2:
            # Check whether we're at the end of one of the lists
            # Append the remainder of the other list to the sorted_list and return it
            if l1 is None and l2 is not None:
                sorted_current.next = l2
                return sorted_head
            if l2 is None and l1 is not None:
                sorted_current.next = l1
                return sorted_head

            # Otherwise continue to the next nodes in the lists
            if l1.val < l2.val:
                sorted_current.next = l1
                l1 = l1.next
            else:
                sorted_current.next = l2
                l2 = l2.next

            sorted_current = sorted_current.next

        return sorted_head
