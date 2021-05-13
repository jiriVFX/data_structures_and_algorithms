# https://leetcode.com/problems/implement-queue-using-stacks/
# Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of a normal queue.
# Implement the MyQueue class:
#
#     void push(int x) Pushes element x to the back of the queue.
#     int pop() Removes the element from the front of the queue and returns it.
#     int peek() Returns the element at the front of the queue.
#     boolean empty() Returns true if the queue is empty, false otherwise.

# O(n) complexity, because in pop() all the remaining elements have to be copied to a new stack
# All other operations are O(1)
class MyQueue(object):

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack_1.append(x)
        print(self.stack_1)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # if there are already items in stack_2
        if len(self.stack_2) > 0:
            front_element = self.stack_2.pop()
            return front_element
        # reverse the order of stack items by popping and appending to stack_2
        elif len(self.stack_1) > 0:
            for _ in range(len(self.stack_1)):
                self.stack_2.append(self.stack_1.pop())

            front_element = self.stack_2.pop()
            return front_element
        else:
            return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # if there are items in first not reversed stack
        if len(self.stack_1) > 0:
            return self.stack_1[0]
        # otherwise return last item from a reversed stack
        elif len(self.stack_2) > 0:
            return self.stack_2[len(self.stack_2) - 1]
        else:
            return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack_2) == 0 and len(self.stack_1) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
my_queue = MyQueue()
my_queue.push("Jiri")
my_queue.push(5)
my_queue.push(8)
my_queue.push(10)
print(my_queue.peek())
print(my_queue.pop())
print(my_queue.stack_2)
print(my_queue.pop())
print(my_queue.stack_2)
my_queue.pop()
print(my_queue.stack_2)
my_queue.pop()
print(my_queue.stack_2)
# param_4 = obj.empty()