# Selection sort O(n^2) - super inefficient, space complexity O(1)

def select_sort(num_list):
    """Selection sort. Takes a list of integers as an argument, returns the sorted list."""
    list_length = len(num_list)
    for i in range(list_length):
        smallest_id = i
        # Start from the next index after the smallest_id
        for j in range(i + 1, list_length):
            if num_list[j] < num_list[smallest_id]:
                # Save the index of the current smallest number
                smallest_id = j
        # Swap the smallest number with the first number of the unsorted part of the list
        # Unsorted part of the list starts with the current i (everything before that is already sorted)
        temp = num_list[i]
        num_list[i] = num_list[smallest_id]
        num_list[smallest_id] = temp
    return num_list


numbers = [13, 33, 6, 187, 1, 5, 89, 56, 2, 11]

print(f"Unsorted input: {numbers}")
print(f"Sorted output:  {select_sort(numbers)}")
