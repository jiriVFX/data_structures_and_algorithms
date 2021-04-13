# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.
# It is guaranteed that there are no cycles anywhere in the entire linked structure.
# Note that the linked lists must retain their original structure after the function returns.

# Follow up: Could you write a solution that runs in O(n) time and use only O(1) memory?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution1 - use set for visited nodes
# O(n) time complexity, O(m * n) space complexity
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        current_a = headA
        current_b = headB
        nodes_set = set()

        # even when we reached the end of one of the lists,
        # we have to continue until we reach end of both lists
        while current_a or current_b:
            if current_a is not None and current_a in nodes_set:
                return current_a
            elif current_b is not None and current_b in nodes_set:
                return current_b
            else:
                # if the two nodes are the same, it is an intersection
                # both nodes can't be None, the loop would exit otherwise
                if current_a == current_b:
                    return current_a
                else:
                    if current_a is not None:
                        nodes_set.add(current_a)
                        current_a = current_a.next
                    if current_b is not None:
                        nodes_set.add(current_b)
                        current_b = current_b.next

        return None
