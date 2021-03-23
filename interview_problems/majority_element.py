# https://leetcode.com/problems/majority-element/
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Time complexity O(n)
# Space complexity O(n)
def majorityElement(nums):
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


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(majorityElement([3, 2, 3]))
print(majorityElement([1]))