# https://leetcode.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

# Solution 1 - brute force - Time Limit Exceeded on LeetCode
# O(n^2) time complexity, O(1) space complexity
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    trapped_rainwater = 0
    # We start from the second element and finish one before the last element
    for i in range(1, len(height) - 1):
        # the amount of water the current element can trap
        # minimum height of the border elements - current element's height
        left = i - 1
        right = i + 1
        # maximums have to start at value of i, they can't be smaller than height i
        max_left = i
        max_right = i
        # move two pointers to the left and right to find maximum height on each side
        while left >= 0 or right <= len(height) - 1:
            if left >= 0:
                if height[left] > height[max_left]:
                    max_left = left
            if right <= len(height) - 1:
                if height[right] > height[max_right]:
                    max_right = right

            left -= 1
            right += 1

        # max_left and max_right are now the largest heights in the list on both sides of i
        # the water we can trap is minumum height of the two max heights minus current height of i
        rainwater = min(height[max_left], height[max_right]) - height[i]

        # add rainwater trapped at the current position to the overal results
        trapped_rainwater += rainwater

    return trapped_rainwater


# print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# print(trap([4, 2, 0, 3, 2, 5]))


# Solution 2 - dynamic programming - optimized solution 1
# O(n) time complexity, O(n) space complexity
def trap_2(height):
    """
    :type height: List[int]
    :rtype: int
    """
    trapped_rainwater = 0

    # store maximum height for each positon
    max_height = 0
    max_left = []
    # find maximum from the left
    for i in range(len(height)):
        if height[i] > max_height:
            max_height = height[i]
        # add current max value to max_left
        max_left.append(max_height)

    max_height = 0
    max_right = []
    # find maximum from the right
    # the values in max_right will be backwards, we have to be careful about that later
    # we could avert this by creating a full length max_right list with 0 values first
    # and then rewriting the values starting from the end of the list instead of appending
    for i in range(len(height) - 1, - 1, - 1):
        if height[i] > max_height:
            max_height = height[i]
        # add current max value to max_left
        max_right.append(max_height)

    # print(max_left)
    # print(max_right)
    # Now we just check each position against our max_heights lists
    # to find the max amount of water that can be trapped
    for i in range(1, len(height) - 1):
        # traverse max_right from the opposite end (the values are backwards, therefore => len(height) - 1 - i)
        # trapped rainwater is minimum of max_left and max_right minus current height
        rainwater = min(max_left[i], max_right[len(height) - 1 - i]) - height[i]

        # add rainwater trapped at the current position to the overal result
        trapped_rainwater += rainwater

    return trapped_rainwater


print(trap_2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap_2([4, 2, 0, 3, 2, 5]))
