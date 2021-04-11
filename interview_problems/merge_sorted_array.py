# https://leetcode.com/problems/merge-sorted-array/
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has a size equal to m + n
# such that it has enough space to hold additional elements from nums2.

# Solution 1
# O(n^2) time complexity, O(1) space complexity
# as we have to modify nums1 in-place, we can't use extra list for the sorting
# the time complexity is thus higher, as we have to move items in nums1 during merging
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0

    while j < n:
        # if we iterated through nums1
        if i >= m:
            nums1[i] = nums2[j]
            i += 1
            j += 1
        # if we iterated through nums2
        elif j >= n:
            return
        # otherwise keep iterating over both
        else:
            # if nums1[i] is smaller or equal to nums2[j], it stays in place
            if nums1[i] <= nums2[j]:
                i += 1
            # if nums2[j] is smaller, it is copied over to nums1[i]
            else:
                # all other items behind nums1[i] have to be moved starting from the end of the list (m)
                # we iterate backwards - the last item is length of both list (m + n) minus 1
                # the first item is i
                for k in range(m, i, -1):
                    nums1[k] = nums1[k - 1]

                nums1[i] = nums2[j]
                j += 1
                # i has to be increased by 1 - original item has moved by 1 to make space for item from nums2
                i += 1
                # number of items in nums1 was increased
                m += 1


list1 = [4, 5, 6, 0, 0, 0]
list2 = [1, 2, 3]

list3 = [1]
list4 = []

print(f"nums1 = {list1}")
print(f"nums2 = {list2}")

merge(nums1=list1, m=3, nums2=list2, n=3)

print(f"nums2 merged in nums1 = {list1}")

# # Solution 2 (by Eric Welch)
# # Not what would interviewers look for, but practically the easiest and simplest
# def merge2(nums1, m, nums2, n):
#     nums1[m:] = nums2[:n]
#     nums1.sort()
#
#
# print(f"nums1 = {list1}")
# print(f"nums2 = {list2}")
#
# merge2(nums1=list1, m=3, nums2=list2, n=3)
#
# print(f"nums2 merged in nums1 = {list1}")
