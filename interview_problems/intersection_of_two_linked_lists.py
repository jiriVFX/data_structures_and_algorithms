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
        # if both pointers reach the end of the list, there is no intersection
        return None


# Solution2
# O(n) time complexity, O(1) space complexity
class Solution2(object):
    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        current_a = headA
        current_b = headB

        while current_a or current_b:
            # if the two pointers meet, current node is intersection
            if current_a is current_b:
                return current_a

            if current_a is None:
                # if at the end, start over from headB
                current_a = headB
            else:
                current_a = current_a.next

            if current_b is None:
                # if at the end, start over from headA
                current_b = headA
            else:
                current_b = current_b.next
        # if both pointers reach the end at the same time, there is no intersection
        return None
