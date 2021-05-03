# https://leetcode.com/problems/container-with-most-water/
# Given n non-negative integers a1, a2, ..., an ,
# where each represents a point at coordinate (i, ai). n vertical lines are drawn
# such that the two endpoints of the line i is at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.

# Solution 1 - brute force - Time Limit Exceeded on LeetCode
# O(n^2) time complexity, O(1) space complexity
def max_area(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_water = 0

    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            # amount of water is minimum height of the two * width
            water = min(height[i], height[j]) * (j - i)
            # if current water is higher than max_water, it is the new max_water
            max_water = max(max_water, water)

    return max_water


# print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# print(max_area([1, 1]))
# print(max_area([4, 3, 2, 1, 4]))
# print(max_area([1, 2, 1]))


# Solution 2 - two pointers
# O(n) time complexity, O(1) space complexity
def max_area_2(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_water = 0
    left = 0
    right = len(height) - 1

    while left < right:
        # amount of water is minimum height of the two * width
        water = min(height[left], height[right]) * (right - left)
        # if current water is higher than max_water, it is the new max_water
        max_water = max(max_water, water)

        # move the pointer with less height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


print(max_area_2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_area_2([1, 1]))
print(max_area_2([4, 3, 2, 1, 4]))
print(max_area_2([1, 2, 1]))
