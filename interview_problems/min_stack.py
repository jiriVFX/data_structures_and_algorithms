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


# Solution 2 - using two stacks - optimized
# O(1) time complexity, O(n) space complexity (but lower on average compared to the Solution 1)
class MinStack2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # Min stack will include list with min items [min value, times of sequential appearance] - e.g. [-3, 2]
        self.min_stack = []
        self.min = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.min is None:
            self.min = val
            self.min_stack.append([val, 1])
        # Check if val is the new minimum (lower than the last item in the min_stack)
        elif val < self.min:
            self.min = val
            self.min_stack.append([val, 1])
        # If the current val is the same as self.min
        elif val == self.min:
            self.min_stack[len(self.min_stack) - 1][1] += 1

    def pop(self):
        """
        :rtype: None
        """
        # pop stack
        popped = self.stack.pop()
        # pop min_stack

        if popped == self.min:
            # If there are more than one of popped items at the end of min_stack
            if self.min_stack[len(self.min_stack) - 1][1] > 1:
                self.min_stack[len(self.min_stack) - 1][1] -= 1
            # Otherwise remove popped item from min_stack and refresh self.min value
            else:
                self.min_stack.pop()
                # New minimum is the last item in min stack, if there's any
                if len(self.min_stack) > 0:
                    self.min = self.min_stack[len(self.min_stack) - 1][0]
                else:
                    self.min = None

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
            return self.min
        return None


# Test examples
print("Solution 2")
min_stack2 = MinStack2()
min_stack2.push(-2)
min_stack2.push(0)
min_stack2.push(-3)
print(min_stack2.getMin())
min_stack2.pop()
print(min_stack2.top())
print(min_stack2.getMin())

# Expected output [null, null, null, null, -3, null, 0, -2]
