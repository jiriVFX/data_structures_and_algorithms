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
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        temp_stack = [x]
        self.stack = temp_stack + self.stack
        print(self.stack)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack) > 0:
            front_element = self.stack[len(self.stack)-1]
            self.stack = self.stack[0:len(self.stack)-1]
            return front_element
        else:
            return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack) == 0:
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
my_queue.pop()
print(my_queue.stack)
print(my_queue.pop())
print(my_queue.stack)
my_queue.pop()
print(my_queue.stack)
my_queue.pop()
print(my_queue.stack)
# param_4 = obj.empty()
