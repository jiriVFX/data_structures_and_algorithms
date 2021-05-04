# https://leetcode.com/problems/backspace-string-compare/
# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Solution 1 - naive brute force
# O(a + b) time complexity, O(a + b) space complexity (actually higher as string slicing creates a copy of the string)
def backspace_compare(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # iterate over s
    output_s = clean_string(s)
    # iterate over t
    output_t = clean_string(t)

    # compare the two strings
    if output_s == output_t:
        return True
    return False


def clean_string(str_to_clean):
    output = ""
    for i in range(len(str_to_clean)):
        if str_to_clean[i] == "#":
            if len(output) > 0:
                output = output[:len(output) - 1]
        else:
            output += str_to_clean[i]
    return output


# print(backspace_compare("ab#c", "ad#c"))
# print(backspace_compare("ab##", "c#d#"))
# print(backspace_compare("a##c", "#a#c"))
# print(backspace_compare("a#c", "b"))
# print(backspace_compare("bxj##tw", "bxj###tw"))


# Solution 2 - two pointers
# O(a + b) time complexity, O(1) space complexity
def backspace_compare_2(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # iterate over strings backwards
    pointer_s = len(s) - 1
    pointer_t = len(t) - 1
    counter_s = 0
    counter_t = 0

    while pointer_s >= 0 or pointer_t >= 0:
        while pointer_s >= 0:
            # if current char is #, move the pointer and increase counter of backspaces
            if s[pointer_s] == "#":
                pointer_s -= 1
                counter_s += 1
            # if current char is valid character, but there are backspaces in the counter,
            # move the pointer and decrease backspace counter
            elif counter_s > 0:
                pointer_s -= 1
                counter_s -= 1
            else:
                # if it is actual valid not to be deleted character
                break

        while pointer_t >= 0:
            # if current char is #, move the pointer and increase counter of backspaces
            if t[pointer_t] == "#":
                pointer_t -= 1
                counter_t += 1
            # if current char is valid character, but there are backspaces in the counter,
            # move the pointer and decrease backspace counter
            elif counter_t > 0:
                pointer_t -= 1
                counter_t -= 1
            else:
                # if it is actual valid not to be deleted character
                break

        # both pointers are either < 0 or at characters that we can check against each other
        # check whether chars at pointer_s and pointer_t equal
        if pointer_s >= 0 and pointer_t >= 0:
            if s[pointer_s] != t[pointer_t]:
                return False
        # if only one of the pointers is less than 0
        if pointer_s < 0 and pointer_t >= 0 or pointer_s >= 0 and pointer_t < 0:
            return False

        # move both pointers if current characters equal
        pointer_s -= 1
        pointer_t -= 1

    return True


print(backspace_compare_2("ab#c", "ad#c"))
print(backspace_compare_2("ab##", "c#d#"))
print(backspace_compare_2("a##c", "#a#c"))
print(backspace_compare_2("a#c", "b"))
print(backspace_compare_2("bxj##tw", "bxj###tw"))
print(backspace_compare_2("aaa###a", "aaaa###a"))
