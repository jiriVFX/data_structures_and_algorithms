# + Good when we have less memory
# + Fast insertion
# + Fast Deletion
# - Not good for searching - we always have to go one by one from the head to tail

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # Optional methods
    # def get_next(self):
    #     return self.next
    #
    # def set_next(self, new_node):
    #     self.next = new_node
    #
    # def get_data(self):
    #     return self.data
    #
    # def set_data(self, new_data):
    #     self.data = new_data


class LinkedList:
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
        # If this is the first element, make it the tail too
        if self.tail is None:
            self.tail = new_node
        # Next item is what what first item was until now
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
                self.length -= 1
                return f"Item at index {index} was removed."
            else:
                # Loop through the list until you get to the position before desired index (index-1)
                while index - 1 > current_position:
                    current_item = current_item.next
                    current_position += 1
                # Current_position == index - 1
                # current_item is the node after which is the node to be removed
                # First we connect next node of the node to be removed to the current_item
                if current_item.next.next is not None:
                    current_item.next = current_item.next.next
                else:
                    current_item.next = None
                    self.tail = current_item
                # List is now one node shorter
                self.length -= 1
                return f"Item at index {index} was removed."
        else:
            return "Index is out of range."

    def reverse(self):
        if self.head is None or self.head.next is None:
            return self.head
        else:
            first = self.head
            # Head becomes the tail
            self.tail = self.head
            second = first.next

            while second is not None:
                # Difficult to understand without drawing on the paper
                # Draw a list on the paper and go number by number
                temp = second.next
                # When second is the end of the list
                if temp is not None:
                    print(f"temp = {temp.data}")
                else:
                    print(f"temp = None")

                second.next = first
                print(f"second.next = {first.data}")
                first = second
                print(f"first = {second.data}")
                second = temp
                # When temp is after the end of the list = None
                if temp is not None:
                    print(f"second = {temp.data}")
                else:
                    print(f"second = None")
            # Head is now the tail and there is nothing after it
            # self.head.next points to what is now the previous node
            # Not using self.head.next = None would result in infinite loop
            self.head.next = None
            self.head = first


my_linked_list = LinkedList()

my_linked_list.append("Cindy")
my_linked_list.append("Martin")
my_linked_list.append("Michael")
my_linked_list.append("Tom")
print(my_linked_list.print_list())
# print(my_linked_list.tail.data)
# my_linked_list.insert_item(2, "Inserted item")
# print(my_linked_list.remove(3))
# print(my_linked_list.tail.data)
my_linked_list.reverse()
print(my_linked_list.print_list())
# my_linked_list.find("Anakin Skywalker")