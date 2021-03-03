# Insertion sort O(n^2) - can be O(n) in the best case with nearly sorted data, space complexity O(1)

def insert_sort(num_list):
    """Insertion sort. Takes a list of integers as an argument, returns the sorted list."""
    for i in range(1, len(num_list)):
        for j in range(i, 0, -1):
            if num_list[j] < num_list[j-1]:
                # If the previous number num_list[j-1] is larger, swap the two
                temp = num_list[j]
                num_list[j] = num_list[j-1]
                num_list[j-1] = temp
    return num_list


numbers = [13, 33, 6, 187, 1, 5, 89, 56, 2, 11]

print(f"Unsorted input: {numbers}")
print(f"Sorted output:  {insert_sort(numbers)}")
