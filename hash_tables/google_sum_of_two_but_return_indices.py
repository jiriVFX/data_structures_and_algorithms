# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.


# Brute force nested loops solution

def twoSum_brute(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# ----------------------------------------------------------------------------------------------------------------------
# Hash table - dictionary solution

def twoSum_hash(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}

    for i in range(len(nums)):
        if nums[i] not in seen:
            seen[target - nums[i]] = i
        else:
            return [seen[nums[i]], i]
    return False


print(twoSum_hash([3, 2, 4], 6))
