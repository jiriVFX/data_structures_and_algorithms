# https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

# # Solution 1 - Naive brute force - Time limit exceeded on LeetCode
# # O(n^3) time complexity, O(1) space complexity
import math


# def max_subarray(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     # -math.inf has to be replaced with -float("inf") on LeetCode (their Python version is older)
#     max_sum = -math.inf
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             total = 0
#             for k in range(i, j + 1):
#                 total += nums[k]
#                 if total > max_sum:
#                     max_sum = total
#     return max_sum
#
#
# print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(max_subarray([1]))
# print(max_subarray([5, 4, -1, 7, 8]))
# print(max_subarray([-1]))


# # Solution 2 - Optimized brute force - Yet again, Time limit exceeded on LeetCode
# # O(n^2) time complexity, O(n) space complexity
# def max_subarray2(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     max_sum = nums[0]
#     for i in range(0, len(nums)):
#         total = 0
#         for j in range(i, len(nums)):
#             # Every new sum is the previous sum + next number in nums
#             total += nums[j]
#             if total > max_sum:
#                 max_sum = total
#     return max_sum
#
#
# print(max_subarray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(max_subarray2([1]))
# print(max_subarray2([5, 4, -1, 7, 8]))
# print(max_subarray2([-1]))


# Solution 3 - Dynamic programming
# O(n) time complexity, O(n) space complexity
def max_subarray3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum_list = [nums[0]]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        # If sum of previous largest possible sum and current number is higher than current number alone
        if nums[i] + sum_list[i - 1] > nums[i]:
            sum_list.append(nums[i] + sum_list[i - 1])
        else:
            sum_list.append(nums[i])
        # Check if the current maximum sum is larger than the previous one
        if sum_list[i] > max_sum:
            max_sum = sum_list[i]
    return max_sum


print(max_subarray3([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray3([1]))
print(max_subarray3([5, 4, -1, 7, 8]))
print(max_subarray3([-1]))


# Solution 4 - Dynamic programming
# O(n) time complexity, O(1) space complexity
def max_subarray3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    last_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        # If sum of previous largest possible sum and current number is higher than current number alone
        if nums[i] + last_sum > nums[i]:
            last_sum = nums[i] + last_sum
        else:
            last_sum = nums[i]
        # Check if the current maximum sum is larger than the previous one
        if last_sum > max_sum:
            max_sum = last_sum
    return max_sum


print(max_subarray3([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray3([1]))
print(max_subarray3([5, 4, -1, 7, 8]))
print(max_subarray3([-1]))
