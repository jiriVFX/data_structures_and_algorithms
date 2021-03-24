# https://leetcode.com/problems/roman-to-integer/
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Given a roman numeral, convert it to an integer.
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
def roman_to_int(s):
    """
    :type s: str
    :rtype: int
    """
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    integer_num = 0
    i = 0
    while i < len(s):
        # Check whether the current numeral has lower value than the next one
        if (i + 1 < len(s)) and roman_dict[s[i]] < roman_dict[s[i + 1]]:
            integer_num += roman_dict[s[i + 1]] - roman_dict[s[i]]
            i += 1
        # Otherwise convert the current numeral into integer
        else:
            integer_num += roman_dict[s[i]]
        i += 1
    return integer_num


print(roman_to_int("III"))
print(roman_to_int("IV"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))