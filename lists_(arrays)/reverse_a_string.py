# Implement functions that reverse a string, one with iteration and the other with recursion.
# Iterative
def reverse_a_string(string):
    if type(string) == str and len(string) > 1:
        reversed_string = ""
        for i in range(1, len(string) + 1):
            reversed_string += string[len(string) - i]
        return reversed_string
    else:
        return "Input is not a valid string longer than 1 char."


print(reverse_a_string("Hello, my name is Jirka."))


# ----------------------------------------------------------------------------------------------------------------------
# Iterative 2
# Easy version (Using slice function [start:stop:step])

def reverse_a_string_easy(string):
    if type(string) == str and len(string) > 1:
        return string[::-1]
    else:
        return "Input is not a valid string longer than 1 char."


print(reverse_a_string_easy("Hello, my name is Jirka."))


# ----------------------------------------------------------------------------------------------------------------------
# Recursive

def reverse_a_string_rec(string):
    if type(string) == str and len(string) >= 1:
        return reverse_a_string_rec(string[1:]) + string[0]
    else:
        return string


print(reverse_a_string_rec("Hello, my name is Jirka."))
