# https://leetcode.com/problems/move-zeroes/
# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.

# O(n) time complexity, pop itself is O(n-1), so the worst case is actually O(n^2)
def move_zeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    zeroes = 0
    while i < len(nums) - zeroes:
        print(nums[i])
        if nums[i] == 0:
            nums.append(nums.pop(i))
            zeroes += 1
        else:
            i += 1


num_list = [0, 0, 1]
move_zeroes(num_list)
print(num_list)
