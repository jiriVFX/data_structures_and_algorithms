# https://leetcode.com/problems/next-permutation/
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible,
# it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

# Solution 1 - LeetCode solution
# O(n) time complexity, O(1) space complexity
def next_permutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # find out if numbers in a list are descending
    i = len(nums) - 1
    # nums are in descending order
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    # if numbers are in descending order
    if i == 0:
        nums.reverse()
        return nums

    # i - 1 is the first "ascending" position from the left
    first_idx = i - 1
    # print(k)

    # swap the first ascending number with the number at previous index
    j = len(nums) - 1
    while nums[j] <= nums[first_idx]:
        j -= 1
    temp = nums[first_idx]
    nums[first_idx] = nums[j]
    nums[j] = temp

    # reverse the right side of swapped numbers (might be necessary like with [2, 3, 1])
    left = first_idx + 1
    right = len(nums) - 1
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp

        left += 1
        right -= 1

    return nums


print(next_permutation([1, 2, 3]))
print(next_permutation([3, 2, 1]))
print(next_permutation([1, 1, 5]))
print(next_permutation([1]))
print(next_permutation([1, 3, 2]))
print(next_permutation([2, 1, 3]))
print(next_permutation([1, 2]))
print(next_permutation([2, 3, 1]))
