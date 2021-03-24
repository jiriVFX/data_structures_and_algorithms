# https://leetcode.com/problems/fizz-buzz/
# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

def fizz_buzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    numbers = []
    for i in range(1, n + 1):
        current = ""
        if i % 3 == 0:
            current += "Fizz"
        if i % 5 == 0:
            current += "Buzz"
        if current == "":
            current = str(i)
        numbers.append(current)
    print(numbers)


fizz_buzz(15)
