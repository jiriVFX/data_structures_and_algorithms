# Quick sort - O(n^2) when picking a bad pivot, but O(n log n) on average. Space complexity O(log n)
# Simple implementation with slightly higher space complexity (creating extra lists for sorting)

# Solution 1 - using extra space, not in-place
def quick_sort_1(num_list):
    """Quick sort. Takes a list of integers as an argument, returns the sorted list."""
    right_side = []
    left_side = []
    length = len(num_list)
    if length > 1:
        # Take the last item as a pivot
        pivot = num_list[length - 1]
        for i in range(length - 1):
            if num_list[i] > pivot:
                right_side.append(num_list[i])
            else:
                left_side.append(num_list[i])
        # Sort the left and right side of the pivot
        return quick_sort_1(left_side) + [pivot] + quick_sort_1(right_side)
    return num_list


numbers = [13, 33, 6, 187, 1, 5, 89, 56, 2, 11]


# print(f"Unsorted input: {numbers}")
# print(f"Sorted output:  {quick_sort_1(numbers)}")


# Solution 2 - in-place sorting
def swap(num_list, i, j):
    temp = num_list[i]
    num_list[i] = num_list[j]
    num_list[j] = temp


def quick_sort_2(num_list, left, right):
    # choose pivot as the last item in the list
    pivot = right
    i = left
    j = left

    while i <= j <= pivot:
        # check every num against pivot
        # if j is at pivot's position, swap items at i and and pivot
        if j == pivot:
            swap(num_list, i, pivot)
            # call self to sort the left of pivot
            quick_sort_2(num_list, left, i - 1)
            # call self to sort the right of pivot
            quick_sort_2(num_list, i + 1, right)
        else:
            # if j is on the left of pivot,
            # and num_list[j] < num_list[pivot], swap items at i and j
            if num_list[j] < num_list[pivot]:
                swap(num_list, i, j)
                # advance i
                i += 1

        # advance j
        j += 1
    # return sorted list
    return num_list


print(f"Unsorted input: {numbers}")
print(f"Sorted output:  {quick_sort_2(numbers, 0, len(numbers) - 1)}")
