# Max-heap implemented as priority queue
# the largest value in the heap is always the root - first in the list (array)
# Formulas for finding parent and child nodes in the list:
#   parent = (index - 1) // 2
#   left_child = (index * 2) + 1
#   right_child = (index * 2) + 2

class MaxHeap:
    def __init__(self, heap_list=[]):
        self.heap_list = heap_list

    def print(self):
        print(self.heap_list)

    def peek(self):
        if len(self.heap_list) > 0:
            return self.heap_list[0]
        else:
            return None

    def is_empty(self):
        if len(self.heap_list) == 0:
            return True
        return False

    def length(self):
        return len(self.heap_list)

    def swap(self, a, b):
        temp = self.heap_list[a]
        self.heap_list[a] = self.heap_list[b]
        self.heap_list[b] = temp

    # O(log n - height of the tree) time complexity, O(n) space complexity
    def pop(self):
        if len(self.heap_list) > 0:
            # store popped item to return it at the end
            popped = self.heap_list[0]

            if len(self.heap_list) > 1:
                # swap the first and the last elements
                self.heap_list[0] = self.heap_list[-1]
            # remove the last element
            self.heap_list.pop()
            # sift to make sure root is the largest value
            self.sift_down()

            return popped

    # O(log n - height of the tree) time complexity, O(n) space complexity
    def add(self, item):
        self.heap_list.append(item)
        self.sift_up()

    def sift_up(self):
        i = len(self.heap_list) - 1

        while True:
            parent = (i - 1) // 2

            if parent < 0:
                break
            # check whether child's value is larger than its parent's value
            # swap the child and the parent until reaching beginning of the list
            if self.heap_list[i] > self.heap_list[parent]:
                self.swap(parent, i)
                # continue from parents position and skip other nodes
                i = parent
            else:
                break

    def sift_down(self):
        i = 0

        while i < len(self.heap_list) - 1:
            left_child = (i * 2) + 1
            right_child = (i * 2) + 2

            if left_child >= len(self.heap_list):
                break

            # choose the child with the larger value
            # check whether its value is larger than its parent's value
            # swap the child and the parent until reaching end of the list
            if right_child < len(self.heap_list) and self.heap_list[right_child] > self.heap_list[left_child]:
                if self.heap_list[i] < self.heap_list[right_child]:
                    self.swap(i, right_child)
                    # move pointer to original left child position
                    i = right_child
                else:
                    break
            else:
                if self.heap_list[i] < self.heap_list[left_child]:
                    self.swap(i, left_child)
                    # move pointer to original right child position
                    i = left_child


max_heap = MaxHeap([80, 76, 60, 49, 42, 15, 24, 40, 35])
print(max_heap.pop())
max_heap.print()
print(max_heap.pop())
max_heap.print()
max_heap.add(46)
max_heap.print()
max_heap.add(51)
max_heap.print()
print(max_heap.peek())
print(max_heap.is_empty())
