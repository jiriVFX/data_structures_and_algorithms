# Binary search can be used to find an item in a sorted list(array)
# O(log n) time complexity
# O(1) space complexity
def binary_search(num_list, item_to_find):
    """Binary search. Takes list of numbers and the item to be found as parameters.
    Returns item's index when item was found, otherwise returns -1.
    :type num_list: list[int]
    :type item_to_find: int
    :rtype: int
    """
    left = 0
    right = len(num_list) - 1
    middle = (left + right) // 2

    # divide in halves as long as left an right pointer don't cross each other
    # when right and left cross, the item_to_find is not in the list
    while left <= right:
        if num_list[middle] == item_to_find:
            # if item_to_find has been found, return its position (the middle pointer)
            return middle
        elif item_to_find > num_list[middle]:
            # if the item we search for is larger than the middle,
            # search on the right side of the middle
            left = middle + 1
        else:
            # if the item we search for is smaller than the middle,
            # search on the left side of the middle
            right = middle - 1

        # recalculate middle
        middle = (left + right) // 2

    # if item_to_find has not been found, it's not in the list
    return -1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 68]
print(f"Your item is at index {binary_search(nums, 8)}")
print(f"Your item is at index {binary_search(nums, 68)}")
print(f"Your item is at index {binary_search(nums, 0)}")
print(f"Your item is at index {binary_search(nums, 70)}")
