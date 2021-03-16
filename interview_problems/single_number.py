# https://leetcode.com/problems/single-number/
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory
def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # O(2n) time complexity - brute force inefficient approach
    # seen_you_set = set()
    # seen_twice = set()
    # for num in nums:
    #     if num not in seen_you_set:
    #         seen_you_set.add(num)
    #     else:
    #         seen_twice.add(num)
    # for num in nums:
    #     if num not in seen_twice:
    #         return num

    # Following works only when any of the elements appears no more than twice (like in this case)
    # O(n) time complexity, but still using one set -> O(n/2+1) -> O(n) memory
    seen_once = set()
    for i in range(len(nums)):
        if nums[i] in seen_once:
            seen_once.remove(nums[i])
        else:
            seen_once.add(nums[i])
    return seen_once.pop()


print(single_number([4, 1, 2, 1, 2]))
