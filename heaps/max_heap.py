# parent = (index - 1) // 2
# left_child = (index * 2) + 1
# right_child = (index * 2) + 2

class MaxHeap:
    def __init__(self, heap_list=[]):
        self.heap_list = heap_list

    def print(self):
        print(self.heap_list)

    def pop(self):
        # swap the first and the last elements
        self.heap_list[0] = self.heap_list[-1]
        # remove the last element
        self.heap_list.pop()
        # sift to make sure root is the largest value
        self.sift_down()
        self.print()

    def sift_down(self):
        for i in range(len(self.heap_list)):
            left_child = (i * 2) + 1
            right_child = (i * 2) + 2

            if right_child >= len(self.heap_list):
                break

            # choose the child with the larger value
            # check whether its value is larger than its parent's value
            # swap the child and the parent until reaching end of the list
            if self.heap_list[left_child] > self.heap_list[right_child]:
                if self.heap_list[i] < self.heap_list[left_child]:
                    temp = self.heap_list[i]
                    self.heap_list[i] = self.heap_list[left_child]
                    self.heap_list[left_child] = temp
            else:
                if self.heap_list[i] < self.heap_list[right_child]:
                    temp = self.heap_list[i]
                    self.heap_list[i] = self.heap_list[right_child]
                    self.heap_list[right_child] = temp





max_heap = MaxHeap([75, 50, 25, 45, 35, 10, 15, 20, 40])
max_heap.pop()
max_heap.pop()
