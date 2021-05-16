# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Solution 1 - multiple binary searches
# O(log n) time
# O(1) space complexity
def search_range(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # try to find the target in the list
    first_index = binary_search(nums, target, 0, len(nums) - 1)

    if first_index == -1:
        # if the target was not found
        return [-1, -1]

    # search left and right side of the first_index
    left = first_index
    right = first_index
    last_seen_1 = None
    last_seen_2 = None

    # search the left side of the first_index
    while left != -1:
        # keeps last found position of target
        last_seen_1 = left
        left = binary_search(nums, target, 0, left - 1)

    # search the right side of the first_index
    while right != -1:
        # keeps last found position of target
        last_seen_2 = right
        right = binary_search(nums, target, right + 1, len(nums) - 1)

    # return the last position from the left and the last position from the right
    return [last_seen_1, last_seen_2]


# binary search helper method
def binary_search(num_list, item_to_find, left, right):
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


print(search_range([5, 7, 7, 8, 8, 10], 8))
print(search_range([5, 7, 7, 8, 8, 10], 6))
print(search_range([], 0))
