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
    # # find out if numbers in a list are descending
    # descending = True
    # for i in range(1, len(nums)):
    #     if nums[i] > nums[i - 1]:
    #         descending = False
    #         break
    # # if the numbers are descending, sort them
    # if descending:
    #     nums.sort()
    # else:
    #     # find the smallest and second smallest numbers,
    #     # move the second smallest to the position of the smallest on the left
    #     smallest_idx = None
    #     # find the smallest
    #     for i in range(1, len(nums)):
    #         if smallest_idx is None:
    #             smallest_idx = i
    #             continue
    #         if nums[i] <= nums[smallest_idx]:
    #             smallest_idx = i
    #     # find the second smallest
    #     second_idx = None
    #     for i in range(len(nums)):
    #         # second smallest must be smaller than any other number except the smallest number
    #         # it must also have higher index than the smallest number,
    #         # so we always get higher number when swapping the two
    #         # second smallest must not be at index 0, so it can be moved to the left
    #         if nums[i] > nums[smallest_idx] and i > smallest_idx:
    #             # if it's the first time
    #             if second_idx is None:
    #                 second_idx = i
    #             # f it's not the first time
    #             elif nums[i] <= nums[second_idx]:
    #                 second_idx = i
    #
    #     # Now we have both smallest and second smallest numbers' indexes
    #     # The next step is to move the second smallest number to the left
    #     # In case we don't have second_idx, it means we have to insert smallest_idx at the beginning of the list
    #     if second_idx is not None:
    #         temp = nums[smallest_idx]
    #         nums[smallest_idx] = nums[second_idx]
    #         nums[second_idx] = temp
    #     else:
    #         if nums[smallest_idx] > nums[0]:
    #             smallest_num = nums.pop()
    #             # Works only in new versions of Python, doesn't add two lists together on LeetCode
    #             # nums = [smallest_num] + nums
    #             # LeetCode solution (less efficient)
    #             nums.insert(0, smallest_num)
    #         else:
    #             temp = nums[0]
    #             nums[0] = nums[1]
    #             nums[1] = temp
    #
    #             temp = nums[smallest_idx]
    #             nums[smallest_idx] = nums[smallest_idx - 1]
    #             nums[smallest_idx - 1] = temp
    # return nums

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
