# We are using a linked list to build our queue.
# Queues are FIFO (First In - First Out)
# Enqueue, Dequeue and Peek are O(1)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def dequeue(self):
        if self.first is not None:
            self.first = self.first.next
            self.length -= 1
        else:
            # If first is None, the last has to be None too
            self.last = None

    def peek(self):
        if self.first is not None:
            return self.first.value

    def print_queue(self):
        if self.first is not None:
            temp_list = []
            temp_node = self.first
            while temp_node is not None:
                temp_list.append(temp_node.value)
                temp_node = temp_node.next
            print(temp_list)
        else:
            print("Queue is empty.")


new_queue = Queue()

new_queue.enqueue("Jirka")
new_queue.enqueue("Jerry")
new_queue.enqueue("Michal")
new_queue.enqueue("Tom")
new_queue.print_queue()
print(new_queue.length)
print(new_queue.peek())
new_queue.dequeue()
new_queue.print_queue()
new_queue.dequeue()
new_queue.print_queue()
new_queue.dequeue()
new_queue.print_queue()
new_queue.dequeue()

print(new_queue.peek())
