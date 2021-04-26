# https://leetcode.com/problems/copy-list-with-random-pointer/
# A linked list of length n is given such that each node contains an additional random pointer,
# which could point to any node in the list, or null.
# Construct a deep copy of the list.
# The deep copy should consist of exactly n brand new nodes,
# where each new node has its value set to the value of its corresponding original node.
# Both the next and random pointer of the new nodes should point to new nodes in the copied list
# such that the pointers in the original list and copied list represent the same list state.
# None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y,
# then for the corresponding two nodes x and y in the copied list, x.random --> y.
# Return the head of the copied linked list.


# Solution 1
# O(n) time complexity, O(1) space complexity
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        current = head

        # copy nodes inside the original list --------------------------------------------------------------------------

        while current is not None:
            # create new copied node
            new_node = Node(x=current.val, next=current.next)
            # change current.next pointer to the new_node
            current.next = new_node

            # move current to the next after the copied node
            current = current.next.next

        # add random pointers --------------------------------------------------------------------------------------

        # we have to replicate the random pointers for the copied nodes
        # also we have to break pointers of the copied nodes to the original nodes

        current = head
        while current is not None:
            # go to the next copied node - copy is always the node after the current
            copy = current.next
            # random pointer will point to the random node after the original random
            if current.random is not None:
                copy.random = current.random.next
            else:
                copy.random = None

            # go to he next original node
            current = current.next.next

        # break connections of the copied nodes to the original nodes --------------------------------------------------
        # this could probably be done inside previous loop, but it complicates the code

        # second node is the head node of the new copied list inside the original list
        copied_head = head.next
        current = head.next
        # another pointer to return the list to its original state
        current_old = head

        while current is not None:
            # Return original list to its original state
            # pointers for the original list
            if current_old.next is not None:
                current_old.next = current_old.next.next
                current_old = current_old.next
            else:
                current_old.next = None
                current_old = None

            # Separate new list from the original list
            # pointers for the new list
            if current.next is not None:
                current.next = current.next.next
                current = current.next
            else:
                current.next = None
                current = None

        # --------------------------------------------------------------------------------------------------------------
        # current = head.next
        # while current is not None:
        #     print(current.val)
        #     current = current.next

        return copied_head
