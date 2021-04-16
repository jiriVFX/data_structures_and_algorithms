# https://leetcode.com/problems/reverse-bits/
# Reverse bits of a given 32 bits unsigned integer.
# Note that in some languages such as Java, there is no unsigned integer type.
# In this case, both input and output will be given as a signed integer type.
# They should not affect your implementation, as the integer's internal binary representation is the same,
# whether it is signed or unsigned.
# Follow up:
# If this function is called many times, how would you optimize it?

# Solution 1 - Using built-in format() function and reversing the bit string (like with normal string)
# O(1) time complexity (Always going through 32 bits), O(1) space complexity
def reverse_bits(n):
    """
    :type n: int
    :rtype: int
    """
    # format int to a 32 bit string - {0:b} works too, if numbers are not over 32 bits
    bit_string = "{0:032b}".format(n)
    # print(bit_string)
    # reverse the bit string
    reversed_str = bit_string[::-1]
    # return int base 2
    # print(reversed_str)
    result_int = int(reversed_str, 2)

    return result_int


print(reverse_bits(0o0000010100101000001111010011100))


# print(reverse_bits(11111111111111111111111111111101))


# Solution 2 - bit operations
# O(1) time complexity (Always going through 32 bits), O(1) space complexity
def reverse_bits2(n):
    """
    :type n: int
    :rtype: int
    """
    reversed_int = 0
    for i in range(32):
        # shift reversed_int to the left
        reversed_int <<= 1

        # reversed_int bits become one if the bit is already 1 or the first bit in n is 1 (mask & 1)
        # without using OR | we loose all 1 bits in reversed_int
        reversed_int = reversed_int | n & 1

        # print("{0:032b}".format(n))
        # print("{0:032b}".format(reversed_int))

        # shift n to the right
        n >>= 1
    return reversed_int


print(reverse_bits2(0o0000010100101000001111010011100))
# print(reverse_bits2(11111111111111111111111111111101))
