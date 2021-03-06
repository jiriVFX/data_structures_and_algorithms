# Merge sort - O(n log n), stable, space complexity O(n)

def merge_sort(num_list):
    """Merge sort. Takes a list of integers as an argument, returns the sorted list.
    Recursively calls itself to split the list down to single item lists.
    Calls merge function to sort and merge the lists back together again."""
    if len(num_list) == 1:
        return num_list
    # Split the list into left and right
    half_length = int(len(num_list) / 2)
    left = num_list[0:half_length]
    right = num_list[half_length:len(num_list)]
    # Merge and sort left and right together
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    sorted_list = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            sorted_list.append(right[r])
            r += 1
        else:
            sorted_list.append(left[l])
            l += 1
    # Finishing leftovers from the longer list
    while l < len(left):
        sorted_list.append(left[l])
        l += 1
    while r < len(right):
        sorted_list.append(right[r])
        r += 1
    return sorted_list


numbers = [13, 33, 6, 187, 1, 5, 89, 56, 2, 11]

print(f"Unsorted input: {numbers}")
print(f"Sorted output:  {merge_sort(numbers)}")
