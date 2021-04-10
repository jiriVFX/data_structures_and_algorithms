# https://leetcode.com/problems/palindrome-linked-list/
# Given the head of a singly linked list, return true if it is a palindrome.

# Solution 1
# O(2n) time complexity, O(n) space complexity
class Solution(object):
    def is_palindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        nodes = []

        while current:
            nodes.append(current.val)
            current = current.next

        for i in range(len(nodes) // 2):
            if nodes[i] != nodes[len(nodes) - (1 + i)]:
                return False

        return True


# Solution 2 - Reversing second half of the list
# O(n) time complexity, O(1) space complexity

class Solution2(object):
    def is_palindrome2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        # Find the middle of the list
        while slow and fast and fast.next:
            # When fast gets to the end of the list, slow will be in the middle
            fast = fast.next.next
            # previous = slow
            slow = slow.next

        # Reverse the second half of the list
        previous = None
        temp = None

        while slow:
            temp = slow.next
            slow.next = previous
            previous = slow
            slow = temp

        # previous is now the last node
        # compare both halves of the list
        first_half = head
        second_half = previous

        while first_half and second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True
