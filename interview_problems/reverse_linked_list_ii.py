# https://leetcode.com/problems/reverse-linked-list-ii/
# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1 - in-place reversal
# O(N) time complexity, O(1) space complexity
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # linked list 1 -> 2 -> 3 -> 4 -> 5, left = 2, right = 4
        # turn into   1 -> 4 -> -> 3 -> 2 -> 5
        # traverse the linked list from head
        # count each node
        # when left position reached (counter == left), start reversing
        # finish reversing when counter == right meaning right position was reached
        # reconnect non reversed parts of the list with the reversed part
        # e.g. 1 -> 4 and 2 -> 5 now

        if head.next is None:
            return head

        counter = 0
        first = head
        second = head.next
        reversed_tail = None
        reversed_head = None

        while first is not None:
            counter += 1

            if left <= counter < right:
                # start reversing
                temp = second.next
                second.next = first
                first = second
                second = temp
            elif counter >= right:
                # if we are beyond the right, connect the reversed part with the remainder of the linked list
                # second is pointing on the first not yet reversed node e.g. 5
                # reversed_tail could be represented as reversed_head.next.next,
                # but I left it here for better readability
                if reversed_tail is not None:
                    reversed_tail.next = second
                # the end of non reversed list has to point to the first node of the reversed part of the list
                # e.g. 1 has to point to 4
                if reversed_head is not None:
                    reversed_head.next = first
                else:
                    # if reversed head is None, we are reversing from the first item
                    head.next = second
                    head = first
                break
            else:
                # if we haven't reached the left position yet
                # reversed head will be the last node before reversed part of the list
                # it's not actually the head, but the head's previous node e.g. 1
                # necessary to connect non reversed part with the reversed part of the list
                reversed_head = first

                first = first.next
                second = first.next
                # needed to connect reversed part with not reversed part at the end
                reversed_tail = first

        return head
