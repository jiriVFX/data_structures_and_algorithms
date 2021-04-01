# https://leetcode.com/problems/happy-number/
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# We have to keep track of the results -> save results in set
# If any result repeats, it will be an endless cycle

def is_happy(n):
    """
    :type n: int
    :rtype: bool
    """
    results = set()
    digits = str(n)
    sum_of_squares = 0

    while True:
        # Separate digits
        digit_list = []
        # Convert each digit back to int, square it and append to the digit_list
        for i in range(len(digits)):
            digit_list.append(int(digits[i]) ** 2)
        # Sum squares of all digits
        sum_of_squares = sum(digit_list)
        # If sum is 1, it's a happy number
        if sum_of_squares == 1:
            return True
        # If sum is not 1 and not already in results
        elif sum_of_squares not in results:
            results.add(sum_of_squares)
        # If the sum is already in results, it's an endless loop and number is not "happy"
        else:
            return False
        # Convert into string to access separate digits in the next iteration
        digits = str(sum_of_squares)


print(is_happy(19))
print(is_happy(2))