# https://leetcode.com/problems/majority-element/
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Time complexity O(n)
# Space complexity O(n)
def majority_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    if length == 1:
        return nums[0]

    elements = {}
    majority_element = nums[0]

    for i in range(length):
        # If item is in elements, count plus 1
        if nums[i] in elements:
            elements[nums[i]] += 1
            # Check whether nums[i] is the majority element at this point
            if elements[nums[i]] > elements[majority_element]:
                majority_element = nums[i]
        # If items is not in items, add it to items
        else:
            elements[nums[i]] = 1
    return majority_element


print(majority_element([2, 2, 1, 1, 1, 2, 2]))
print(majority_element([3, 2, 3]))
print(majority_element([1]))


# ----------------------------------------------------------------------------------------------------------------------
# The same but with sorting
# Time complexity O(n log n)
# Space complexity O(1)
def majority_element_sort(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    return nums[len(nums) // 2]


print(majority_element_sort([2, 2, 1, 1, 1, 2, 2]))
print(majority_element_sort([3, 2, 3]))
print(majority_element_sort([1]))
