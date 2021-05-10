# https://leetcode.com/problems/linked-list-cycle-ii/
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list
# that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
# Notice that you should not modify the linked list.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1 - remember visited nodes with Set (HashSet)
# O(n) time complexity
# O(n) space complexity - nodes stored in the Set
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None

        seen_nodes = set()
        current = head

        # we traverse the list until encountering node, that is already in seen_nodes
        # or when we reach the end of the list without cycle
        while current not in seen_nodes:
            if current is None:
                return None
            # add current to seen_nodes
            seen_nodes.add(current)
            # continue to the next node
            current = current.next

        return current
