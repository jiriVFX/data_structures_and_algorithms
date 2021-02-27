# + Can be iterated (traversed) both from the front and from the back
# + Good for searching elements
# - More complex
# - Requires more memory - every node has to point to the previous node too now
# - Requires extra operations - we always have to update previous node too now


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    # O(1)
    def get_size(self):
        return self.length

    # Insert at the start of the list #
    # O(1) complexity
    def prepend(self, data):
        new_node = Node(data)
        # If there is a head, its previous pointer has to point to the new node
        if self.head is not None:
            self.head.previous = new_node
        else:
            # If there is no head, this is the first node and it will become a tail too
            self.tail = new_node
        # Next item is what was the first item until now
        new_node.next = self.head
        # new_node becomes the first item now
        self.head = new_node
        # The list is one node longer now
        self.length += 1

    # Append to the end of the list
    # O(1) complexity
    def append(self, data):
        new_node = Node(data)
        # If the list is empty, just make the new_node its head
        if self.head is None:
            self.head = new_node
            # new_node becomes list's tail as it is the only item in the list now
            self.tail = self.head
            # The list is one node longer now
            self.length += 1
        else:
            # Last item of the list becomes previous item of the new_node
            new_node.previous = self.tail
            # Append the new_node to the last item of the list
            self.tail.next = new_node
            # New node is now the last item of the list
            self.tail = new_node
            # The list is one node longer now
            self.length += 1

    # O(n)
    def print_list(self):
        print_list = []
        current_node = self.head
        # Loop through a list as long as there is a next item
        while current_node is not None:
            print_list.append(current_node.data)
            current_node = current_node.next
        return print_list

    # O(n) time complexity
    def insert_item(self, index, data):
        new_node = Node(data)
        current_position = 0
        current_item = self.head

        # Check if index is smaller than the length of the list
        # If not, append new_node to the end of the list
        if index < self.length:
            # If index is 0, the new item becomes head of list
            if index <= 0:
                self.head.previous = new_node
                new_node.next = self.head
                self.head = new_node
                self.length += 1
            else:
                # Loop through the list until you get to the position before desired index (index-1)
                while index - 1 > current_position:
                    current_item = current_item.next
                    current_position += 1
                # Current_position == index - 1
                # current_item is the node after which we will insert the new node
                # First we connect original next node to the new_node
                new_node.next = current_item.next
                # The original next node previous pointer needs to point to the new node
                current_item.next.previous = new_node
                # Second we point current_item.next to the new_node
                current_item.next = new_node
                self.length += 1
        else:
            # Index is out of range, append the data at the end of the list
            self.append(data)

    def find(self, data):
        current_item = self.head
        index = 0
        while current_item is not None:
            if current_item.data == data:
                print(f"{data} found at index {index}")
                return True
            current_item = current_item.next
            index += 1
        print(f"{data} is not in the list.")
        return False

    # O(n) time complexity
    def remove(self, index):
        current_position = 0
        current_item = self.head

        # Check if index is smaller than the length of the list
        if self.length > index >= 0:
            # If index == 0
            if index == 0:
                new_head = self.head.next
                self.head = new_head
                # Remove previous pointer for the new head - there can't be any node before head
                new_head.previous = None
                self.length -= 1
                return f"Item at index {index} was removed."
            else:
                # Loop through the list until you get to the position before desired index (index-1)
                while index - 1 > current_position:
                    current_item = current_item.next
                    current_position += 1
                # Current_position == index - 1
                # current_item is the node after which is the node to be removed
                # the node after the node to be removed needs to point to current_item now
                if current_item.next.next is not None:
                    current_item.next.next.previous = current_item
                    # we connect the next node of the node to be removed to the current_item
                    current_item.next = current_item.next.next
                else:
                    # If there's nothing after current item
                    self.tail = current_item
                    current_item.next = None
                # List is now one node shorter
                self.length -= 1
                return f"Item at index {index} was removed."
        else:
            return "Index is out of range."


my_linked_list = DoublyLinkedList()

my_linked_list.append("Jirka")
my_linked_list.append("Lucy")
my_linked_list.append("Martin")
my_linked_list.append("Tom")
print(my_linked_list.print_list())
# print(my_linked_list.tail.previous.previous.data)
# print(my_linked_list.tail.previous.next.data)
# my_linked_list.insert_item(2, "Inserted item")
print(my_linked_list.remove(3))
print(my_linked_list.print_list())
#my_linked_list.find("Anakin Skywalker")