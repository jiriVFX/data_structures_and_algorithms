# https://leetcode.com/problems/implement-strstr/
# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().

# Solution 1 - Naive approach - Time Limit Exceeded on LeetCode
# O(n^2) time complexity, O(1) space complexity
def str_str(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # if needle is an empty string
    if len(needle) == 0:
        return 0
    # if needle is longer than haystack
    elif len(needle) > len(haystack):
        return -1

    start_index = None

    for i in range(len(haystack)):
        # Reset start_index at every iteration
        start_index = None
        j = i
        n = 0
        # check each char of needle in haystack starting from j (j = i at the start)
        while n < len(needle) and j < len(haystack):
            # if chars equal, record the start index if it's empty
            if haystack[j] == needle[n]:
                if start_index is None:
                    start_index = j
                # increment loop variables
                j += 1
                n += 1
            # break the loop if chars don't equal
            else:
                break

        # if we found all characters in needle
        if n == len(needle):
            return start_index

    # if we get to this point, matching substring wasn't found
    return -1


print(str_str(haystack="hello", needle="ll"))
print(str_str(haystack="aaaaa", needle="bba"))
print(str_str(haystack="", needle=""))
print(str_str(haystack="aaa", needle="aaaa"))
print(str_str(haystack="mississippi", needle="issipi"))
print(str_str(haystack="a", needle="a"))
print(str_str(haystack="abc", needle="c"))


# # Solution 2 - KMP (Knuth–Morris–Pratt algorithm) - Can't make it work for all test cases
# # O(n + m) time complexity (length of haystack * length of needle), O(m) space complexity
# def str_str2(haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     # if needle is an empty string
#     if len(needle) == 0:
#         return 0
#     # if needle is longer than haystack
#     elif len(needle) > len(haystack):
#         return -1
#
#     prefix_suffix = [0]
#     i = 0
#     j = 1
#
#     # Build the prefix-suffix list - find the longest prefix-suffix in needle
#     while j < len(needle):
#         # We search for the same prefix suffix pattern
#         if needle[i] == needle[j]:
#             prefix_suffix.append(i + 1)
#             i += 1
#         else:
#             # i becomes the previous number in prefix_suffix
#             if i > 0:
#                 i = prefix_suffix[i - 1]
#             prefix_suffix.append(0)
#         j += 1
#     print(prefix_suffix)
#
#     # Now we can check for the needle in haystack ----------------------------------------------------------------------
#     i = 0
#     j = 0
#
#     while i < len(haystack) and j < len(needle) and (len(haystack) - i >= len(needle) - j):
#         if haystack[i] == needle[j] or j == 0:
#             print(f"haystack {haystack[i]} == needle {needle[j]}")
#             j += 1
#             print(f"j = {j}")
#             i += 1
#         else:
#             print(f"haystack {haystack[i]} != needle {needle[j]}")
#             # j becomes j - 1 value from prefix_suffix table
#             # so we don't have to always start to search from beginning of the needle
#             if len(prefix_suffix) > 2:
#                 print(f"j = {j}")
#                 j = prefix_suffix[j - 1]# must be +1, otherwise we compare one char behind in the next iteration
#                 print(f"j = {j}")
#
#             # else:
#             #     j = 0
#         # i += 1
#
#     print(f"i {i} - j {j}")
#     if j == len(needle) and i - j >= 0:
#         return i - j
#     else:
#         return -1
#
#
# # print(str_str2(haystack="adsgwadsxdsgwadsgz", needle="dsgwadsgz"))
# # print(str_str2(haystack="hello", needle="ll"))
# # print(str_str2(haystack="aaaaa", needle="bba"))
# # print(str_str2(haystack="", needle=""))
# # print(str_str2(haystack="aaa", needle="aaaa"))
# # print(str_str2(haystack="mississippi", needle="issipi"))
# # print(str_str2(haystack="mississippi", needle="issip"))
# # print(str_str2(haystack="a", needle="a"))
# # print(str_str2(haystack="abc", needle="c"))
# # print(str_str2(haystack="mississippi", needle="pi"))
# print(str_str2(haystack="babba", needle="bbb"))