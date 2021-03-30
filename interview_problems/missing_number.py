# https://leetcode.com/problems/missing-number/
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

# First solution - brute force
# O(n^2) time complexity, O(1) space complexity
def missing_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Create all numbers in the range 0 - length of nums
    # range_set = set(range(0, len(nums) + 1))
    # print(range_set)
    # Check what number is missing from the range_set
    for i in range(0, len(nums) + 1):
        if i not in nums:
            return i


print(missing_number([3, 0, 1]))
print(missing_number([0, 1]))
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))


# Better solution
# O(2n) time complexity, O(n) space complexity
def missing_number2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Create all numbers in the range 0 - length of nums
    range_set = set(range(len(nums) + 1))
    # print(range_set)
    # Remove every number present in both nums and range_set from range_set
    for i in range(len(nums)):
        if nums[i] in range_set:
            range_set.remove(nums[i])
    # What's left must be the missing number
    return range_set.pop()


print(missing_number2([3, 0, 1]))
print(missing_number2([0, 1]))
print(missing_number2([9, 6, 4, 2, 3, 5, 7, 0, 1]))


# Improved previous solution, fastest of all four
# O(n) time complexity, O(n) space complexity
def missing_number2_5(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Create set from nums
    nums_set = set(nums)

    # Check if i is in set
    for i in range(len(nums) + 1):
        if i not in nums_set:
            return i


print(missing_number2_5([3, 0, 1]))
print(missing_number2_5([0, 1]))
print(missing_number2_5([9, 6, 4, 2, 3, 5, 7, 0, 1]))


# Slower than previous one, but more space efficient
# O(n log n + n) time complexity, O(1) space complexity
def missing_number3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Sort nums first
    nums.sort()
    # Check whether i = nums[i]
    for i in range(len(nums)):
        if i != nums[i]:
            return i
    # If all numbers match, than the len(nums) + 1 must be missing
    return i + 1


print(missing_number3([3, 0, 1]))
print(missing_number3([0, 1]))
print(missing_number3([9, 6, 4, 2, 3, 5, 7, 0, 1]))
