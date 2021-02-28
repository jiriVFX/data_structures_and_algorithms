# Find a factorial of any number

# Original recursion function - required a global variable
# result = 1
#
#
# def factorial_rec_old(number):
#     global result
#     if number > 1:
#         result = result * number
#         number -= 1
#         factorial_rec_old(number)
#     return result


# Using a recursion O(n) (if multiplication would be O(1))
def factorial_rec(number):
    """Return factorial of an integer using recursion"""
    if number > 1:
        return number * factorial_rec(number - 1)
    return number


# Using a while loop O(n)
def factorial_loop(number):
    """Return factorial of an integer using a while loop"""
    if type(number) == int:
        result = number
        number -= 1
        while number > 1:
            result = result * number
            number -= 1
        return result
    else:
        return "Invalid type"


# print(factorial_rec_old(5))
print(factorial_rec(5))
print(factorial_loop(5))
