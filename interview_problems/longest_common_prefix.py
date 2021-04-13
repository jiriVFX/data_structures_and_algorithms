# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Solution 1
# O(m * n) time complexity - The longest prefix length * number of strings in the list
# O(1) space complexity
def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) > 1:
        i = 0
        longest_prefix = ""
        while True:
            # if i is larger than length of any of the strings, return longest_prefix
            if i < len(strs[0]):
                # assign current character
                current_char = strs[0][i]

                for j in range(1, len(strs)):
                    # Just for readability
                    current_string = strs[j]

                    # if char i in current string equals current_char, continue to the next string
                    if i < len(current_string) and current_string[i] == current_char:
                        continue
                    # otherwise return current longest_prefix
                    else:
                        return longest_prefix

                # if we've got to this point, we can add current_char to longest_prefix
                longest_prefix += current_char
                # increment i
                i += 1
            else:
                return longest_prefix
    elif len(strs) == 1:
        return strs[0]
    else:
        return ""


print(f'Longest prefix = "{longest_common_prefix(["flower", "flow", "flight"])}"')
print(f'Longest prefix = "{longest_common_prefix(["dog", "racecar", "car"])}"')
print(f'Longest prefix = "{longest_common_prefix(["a"])}"')
