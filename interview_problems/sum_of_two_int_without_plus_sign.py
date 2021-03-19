# https://leetcode.com/problems/sum-of-two-integers/
# Given two integers a and b, return the sum of the two integers without using the operators + and -.
# We have to use bitwise operations
# Python integers can go to infinity, so the mask has to be applied to avoid infinite loop
# https://www.youtube.com/watch?v=qq64FrA2UXQ
# https://www.instructables.com/Convert-Negative-Numbers-to-Binary/

def get_sum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    mask = 0xffffffff
    while b:
        # xor summary
        sum = (a ^ b) & mask
        # & to know where to carry 1
        carry = ((a & b) << 1) & mask
        a = sum
        b = carry

    # If the first bit is 1, it is a negative number
    if (a >> 31) & 1:
        return ~ (a ^ mask)
    return a


print(get_sum(3, 2))
