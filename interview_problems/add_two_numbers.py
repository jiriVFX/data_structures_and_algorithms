# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1
# O(m + n) time complexity, O(n) space complexity
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        number_1 = ""
        number_2 = ""
        sum_result = 0
        # Get the int digits backwards
        while l1 is not None:
            # number_1 = number_1 * 10 + l1.val
            number_1 += str(l1.val)
            l1 = l1.next

        while l2 is not None:
            # number_2 = number_2 * 10 + l2.val
            number_2 += str(l2.val)
            l2 = l2.next

        # reverse the order of the digits
        number_1 = number_1[::-1]
        number_2 = number_2[::-1]

        # sum the two numbers
        sum_result = int(number_1) + int(number_2)
        # reverse the sum
        sum_result = str(sum_result)[::-1]

        # Create a new list ----------------------------------
        head = ListNode(int(sum_result[0]))
        tail = head

        for i in range(1, len(sum_result)):
            new_node = ListNode(int(sum_result[i]))
            tail.next = new_node
            tail = new_node

        return head

