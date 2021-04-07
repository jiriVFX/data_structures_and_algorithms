# https://leetcode.com/problems/count-and-say/
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
# which is then converted into a different digit string.
# To determine how you "say" a digit string,
# split it into the minimal number of groups so that each group is a contiguous section all of the same character.
# Then for each group, say the number of characters, then say the character.
# To convert the saying into a digit string, replace the counts with a number and concatenate every saying.
# Given a positive integer n, return the nth term of the count-and-say sequence.
# Hint: The following are the terms from n=1 to n=10 of the count-and-say sequence:
#  1.     1
#  2.     11
#  3.     21
#  4.     1211
#  5.     111221
#  6.     312211
#  7.     13112221
#  8.     1113213211
#  9.     31131211131221
# 10.     13211311123113112211

# O(2^n) time complexity, O(2^n) space complexity
def count_and_say(n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return "1"
    last_in_sequence = "1"

    for i in range(n - 1):
        new_in_sequence = ""
        digit_counter = 0

        last_digit = last_in_sequence[0]

        # Go through each digit and count it
        for digit in range(len(last_in_sequence)):
            # if the current digit is not the same as the last digit
            # add the last_digit in the new_in_sequence
            if last_digit != last_in_sequence[digit]:
                new_in_sequence += str(digit_counter) + last_digit
                # Reset the counter
                digit_counter = 1
            else:
                digit_counter += 1

            # if digit is the last digit in the current sequence
            if digit == len(last_in_sequence) - 1:
                new_in_sequence += str(digit_counter) + last_in_sequence[digit]

            # The current digit is now the last digit for the next iteration
            last_digit = last_in_sequence[digit]

        # replace previous n-1 sequence item with the new item
        last_in_sequence = new_in_sequence

    return last_in_sequence


print(count_and_say(1))
print(count_and_say(4))
print(count_and_say(6))
print(count_and_say(10))
