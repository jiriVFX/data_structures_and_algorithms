# https://leetcode.com/problems/number-of-1-bits/
# Write a function that takes an unsigned integer
# and returns the number of '1' bits it has (also known as the Hamming weight).

# O(number of 1 bits in n) time complexity, O(1) space complexity
def hamming_weight(n):
    """
    :type n: int
    :rtype: int
    """
    # We continue removing 1 bits until n == 0
    # -1- 0 0 - > 2^2 = 4
    # -0- 1 1 (n - 1 = 4 - 1 = 3) -> current bit becomes 0 (binary 0 1 1)
    # -0- 0 0 - n & (n - 1) - result is 1 only if both n and (n - 1) are 1, which they are not
    # So n & (n - 1) is 1 0 0 & 0 1 1 = 0 0 0
    #
    # Or with number n = 1101, n - 1 = 1100, 1101 & 1100 = 1100 - we remove one 1bit every cycle
    # Next cycle n = 1100, n - 1 = 1011, 1100 & 1011 = 1000
    # The last cycle n = 1000, n - 1 = 0111, 1000 & 0111 = 0000 - we have finished
    count = 0
    while n != 0:
        n = n & (n - 1)
        count += 1
    return count


print(hamming_weight(0o0000000000000000000000000001011))
print(hamming_weight(0o0000000000000000000000010000000))
print(hamming_weight(0o11111111111111111111111111111101))