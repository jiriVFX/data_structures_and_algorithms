# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1 - string reversing - easy
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


# Solution 2 - modulo and division operations
# O(m + n) time complexity, O(n) space complexity
class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        number_1 = 0
        number_2 = 0
        result_sum = 0

        # Extract and reverse l1 and l2 -----------------------

        i = 0
        while l1 is not None:
            number_1 += (10 ** i) * l1.val
            l1 = l1.next
            i += 1

        i = 0
        while l2 is not None:
            number_2 += (10 ** i) * l2.val
            l2 = l2.next
            i += 1

        # reverse digits in result_sum and add to a new list ---------------------------

        # create dummy head of the result list
        head = ListNode(-1)
        tail = head

        result_sum = number_1 + number_2

        if result_sum != 0:
            while result_sum != 0:
                digit = result_sum % 10
                # remove one zero from x
                result_sum = int(result_sum / 10)

                # create new node and add it to the result list
                new_node = ListNode(digit)
                tail.next = new_node
                tail = new_node
        else:
            head.next = ListNode(result_sum)

            # head is dummy, so next is the start of the actual list
        return head.next
