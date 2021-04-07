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

# O(n^3) time complexity, O(1) space complexity
def count_and_say(n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return "1"
    last_in_sequence = "1"

    for i in range(n - 1):
        # print(last_in_sequence)
        new_in_sequence = ""
        digit_counter = {}

        last_digit = last_in_sequence[0]

        # Go through each digit and count it
        for digit in last_in_sequence:
            # if current digit is same as the last one
            if last_digit == digit:
                if digit in digit_counter:
                    digit_counter[digit] += 1
                else:
                    digit_counter[digit] = 1
            else:
                # if the current digit is not same as the last digit
                # write the current digits in the new_in_sequence
                for key, value in digit_counter.items():
                    new_in_sequence += str(value) + key
                # Empty the dictionary
                digit_counter = {}
                # Add the current digit to the counter
                digit_counter[digit] = 1
            # The current digit is now the last digit for the next iteration
            last_digit = digit

        # write the remaining numbers into current sequence
        for key, value in digit_counter.items():
            new_in_sequence += str(value) + key

        # replace previous n-1 sequence item with the new item
        last_in_sequence = new_in_sequence

    return last_in_sequence


print(count_and_say(1))
print(count_and_say(4))
print(count_and_say(6))
print(count_and_say(10))


# O(n^3) time complexity - again the same problem - different output on LeetCode compared to the local machine
def count_and_say1_1(n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return "1"
    last_in_sequence = "1"

    for i in range(n - 1):
        # print(last_in_sequence)
        new_in_sequence = ""
        digit_counter = {}

        last_digit = last_in_sequence[0]

        # Go through each digit and count it
        for digit in range(len(last_in_sequence)):
            # if current digit is the same as the last one and is not the last in last_in_sequence
            if last_digit == last_in_sequence[digit] and digit < len(last_in_sequence) - 1:
                if last_in_sequence[digit] in digit_counter:
                    digit_counter[last_in_sequence[digit]] += 1
                else:
                    digit_counter[last_in_sequence[digit]] = 1
            else:
                # if the current digit is not same as the last digit
                # or if the current digit is the last in the last sequence
                # write the current digits in the new_in_sequence

                if digit == len(last_in_sequence) - 1:
                    # Add the current digit to the counter
                    if last_in_sequence[digit] in digit_counter:
                        digit_counter[last_in_sequence[digit]] += 1
                    else:
                        digit_counter[last_in_sequence[digit]] = 1

                for key, value in digit_counter.items():
                    new_in_sequence += str(value) + key
                # Empty the dictionary
                digit_counter = {}

                if last_digit != last_in_sequence[digit]:
                    # Add the current digit to the counter
                    digit_counter[last_in_sequence[digit]] = 1

            # The current digit is now the last digit for the next iteration
            last_digit = last_in_sequence[digit]

        # replace previous n-1 sequence item with the new item
        last_in_sequence = new_in_sequence

    return last_in_sequence


print(count_and_say1_1(1))
print(count_and_say1_1(4))
print(count_and_say1_1(6))
print(count_and_say1_1(10))
