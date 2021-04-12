# https://leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# Solution 1 - using two stacks
# O(1) time complexity, O(n) space complexity
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        # Check if val is the new minimum (lower than the last item in the min_stack)
        elif val < self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.append(val)
        # Otherwise the new minimum is the same as the last minimum
        else:
            last_min = self.min_stack[len(self.min_stack) - 1]
            self.min_stack.append(last_min)

    def pop(self):
        """
        :rtype: None
        """
        # pop stack
        self.stack.pop()
        # pop min_stack
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) > 0:
            return self.min_stack[len(self.min_stack) - 1]
        return None


# Test examples
print("Solution 1 - using two stacks")
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())
min_stack.pop()
print(min_stack.top())
print(min_stack.getMin())

# Expected output [null, null, null, null, -3, null, 0, -2]
