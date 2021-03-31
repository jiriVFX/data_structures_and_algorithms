# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays
# and you may return the result in any order.

# O(2n) time complexity
# O(2n) space complexity (we are creating num_dict and intersection list)
def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    num_dict = {}
    intersection = []
    # Put all numbers from the first list in dictionary
    # Count appearance of each number
    for num in nums1:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    # Check whether nums in second list are in dictionary
    # If they are, they are intersection of the two lists
    for num in nums2:
        if num in num_dict:
            if num_dict[num] > 0:
                intersection.append(num)
                num_dict[num] -= 1

    return intersection


print(intersect([1, 2, 2, 1], [2, 2]))
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
print(intersect([3, 1, 2], [1, 1]))