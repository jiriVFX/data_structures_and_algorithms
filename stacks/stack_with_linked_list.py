# We are using a linked list to build our stack.
# Stacks are LIFO (Last In - First Out)
# Push, Pop and Peek are O(1)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        node = Node(value)

        if self.top is not None:
            node.next = self.top
        else:
            node.next = self.bottom
            self.bottom = node
        self.top = node
        self.length += 1

    def pop(self):
        if self.length > 0:
            if self.top.next is not None:
                self.top = self.top.next
                self.length -= 1
            else:
                self.top = None
                self.bottom = None
                self.length -= 1

    def peek(self):
        if self.top is not None:
            return self.top.value
        else:
            return None


new_stack = Stack()

new_stack.push("Anakin")
new_stack.push("Padmé")
new_stack.push("Luke")
new_stack.push("Leia")
print(new_stack.top.value)
print(new_stack.bottom.value)
print(new_stack.length)
new_stack.pop()
print(new_stack.peek())
new_stack.pop()
print(new_stack.peek())
new_stack.pop()
print(new_stack.peek())
new_stack.pop()
print(new_stack.peek())
