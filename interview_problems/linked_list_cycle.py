# https://leetcode.com/problems/linked-list-cycle/
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list
# that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1 - using set (hash set)
# O(n) time complexity, O(n) space complexity
class Solution(object):
    def has_cycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        current = head

        while current:
            if current in seen:
                return True

            seen.add(current)
            current = current.next

        return False


# Solution 2 - Floyd’s Cycle-Finding Algorithm
# O(n) time complexity, O(1) space complexity

class Solution2(object):
    def has_cycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
