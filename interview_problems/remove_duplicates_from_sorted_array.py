# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Given a sorted array nums,
# remove the duplicates in-place such that each element appears only once and returns the new length.
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.
# Note that the input array is passed in by reference,
# which means a modification to the input array will be known to the caller as well.

# O(n^2) time complexity - (n time while loop) * (n time removing duplicate elements)
def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1

    return len(nums)


print(remove_duplicates([1]))
print(remove_duplicates([1, 1, 2]))
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


# O(n^2) time complexity
# Should be slightly better than the previous one.
# We don't have to move that many elements in the list when popping an item.
def remove_duplicates2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) > 1:
        i = len(nums) - 2
        while i >= 0:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            i -= 1

    return len(nums)


print(remove_duplicates2([1]))
print(remove_duplicates2([1, 1, 2]))
print(remove_duplicates2([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


# O(n) time complexity
# Without popping elements of the list
def remove_duplicates3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    if len(nums) > 1:
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

    return i + 1


print(remove_duplicates3([1]))
print(remove_duplicates3([1, 1, 2]))
print(remove_duplicates3([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
