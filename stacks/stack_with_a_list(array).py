# We are using a list (an array) to build our stack.
# Stacks are LIFO (Last In - First Out)
# Push, Pop and Peek are O(1)

class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)
        return self.stack_list

    # Renamed to pop_stack to not confuse with inbuilt pop() function for lists
    def pop_stack(self):
        if len(self.stack_list) > 0:
            self.stack_list.pop()
            return self.stack_list

    def peek(self):
        if len(self.stack_list) != 0:
            return self.stack_list[len(self.stack_list)-1]
        else:
            return self.stack_list


new_stack = Stack()

print(new_stack.peek())
print(new_stack.push("Jerry"))
print(new_stack.push("Cindy"))
print(new_stack.push("Michael"))
print(new_stack.push("Justin"))
print(new_stack.peek())
print(new_stack.pop_stack())
print(new_stack.pop_stack())
print(new_stack.pop_stack())
print(new_stack.pop_stack())
