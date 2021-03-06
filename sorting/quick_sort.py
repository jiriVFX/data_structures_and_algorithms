# Quick sort - O(n^2) when picking a bad pivot, but O(n log n) on average. Space complexity O(log n)
# Simple implementation with slightly higher space complexity (creating extra lists for sorting)

def quick_sort(num_list):
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
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    return num_list


numbers = [13, 33, 6, 187, 1, 5, 89, 56, 2, 11]

print(f"Unsorted input: {numbers}")
print(f"Sorted output:  {quick_sort(numbers)}")
