# https://leetcode.com/problems/excel-sheet-column-number/
# Given a string columnTitle that represents the column title as appear in an Excel sheet,
# return its corresponding column number.
def title_to_number(column_title):
    """
    :type column_title: str
    :rtype: int
    """
    title = column_title.lower()
    column_dict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26
    }
    if len(title) == 0:
        return 0
    elif len(title) == 1:
        return column_dict[title]
    # If title has more than one character
    else:
        final_number = 0
        # Go through title character by character
        # First character is always character value
        # Each following character value is final_number * 26 + current character value
        for i in range(len(title)):
            if i == 0:
                final_number = column_dict[title[i]]
            else:
                final_number = final_number * 26 + column_dict[title[i]]
        return final_number


print(title_to_number("AA"))
print(title_to_number("FXSHRXW"))