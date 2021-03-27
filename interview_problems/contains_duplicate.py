# https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# O(n) time complexity, O(1) space complexity
def contains_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    value_set = set()
    for value in nums:
        if value in value_set:
            return True
        else:
            value_set.add(value)
    return False


print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
