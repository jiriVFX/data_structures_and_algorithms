# https://leetcode.com/problems/rotate-array/
# Given an array, rotate the array to the right by k steps, where k is non-negative.


# Solution 1 - using extra list
# O(n) time complexity, O(n) space complexity
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # make sure k is not out of index
    # also prevents from unnecessary rotations
    length = len(nums)
    k = k % length

    # first copy all items, except the last k items, which are going to be rotated
    temp = []
    for i in range(length - k):
        temp.append(nums[i])
    # replace first k items with last k items
    for i in range(k):
        nums[i] = nums[- (k - i)]
    # write the remaining items from temp to nums
    for i in range(length - k):
        nums[k + i] = temp[i]


nums_1 = [1, 2, 3, 4, 5, 6, 7]
nums_2 = [-1, -100, 3, 99]
nums_3 = [-1]
nums_4 = [1, 2]

# rotate(nums_1, 3)
# rotate(nums_2, 2)
# rotate(nums_3, 2)
# rotate(nums_4, 3)
# print(nums_1)
# print(nums_2)
# print(nums_3)
# print(nums_4)


# Solution 2 - cyclic replacements
# O(n) time complexity, O(1) space complexity
def rotate_2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # make sure k is not out of index
    # also prevents from unnecessary rotations
    length = len(nums)
    k = k % length

    start_pos = 0
    count = 0
    while count < length:
        current_pos = start_pos
        # first item from the list goes to temp
        current_item = nums[start_pos]
        while True:
            # get new position for current_item in nums
            new_pos = (current_pos + k) % length
            # copy item at that position to temp before it gets replaced by current item
            temp = nums[new_pos]
            # write the previous temp to its new position
            nums[new_pos] = current_item

            # current_item becomes temp for the next iteration
            current_item = temp
            current_pos = new_pos
            count += 1

            # move item until you get to the starting position
            if start_pos == current_pos:
                break
        # move to the next index
        start_pos += 1


rotate_2(nums_1, 3)
rotate_2(nums_2, 2)
rotate_2(nums_3, 2)
rotate_2(nums_4, 3)
print(nums_1)
print(nums_2)
print(nums_3)
print(nums_4)
