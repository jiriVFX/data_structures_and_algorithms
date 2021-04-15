# Hackerrank problem
# Determine the maximum positive spread for a stock given its price history
# If the stock remains flat or declines for the full period, return -1


# Complete the 'maxDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY px as parameter.
#

def maxDifference(px):
    min_price = px[0]
    max_profit = 0

    for i in range(1, len(px)):
        if px[i] < min_price:
            min_price = px[i]
        if px[i] - min_price > max_profit:
            max_profit = px[i] - min_price

    if max_profit < 1:
        return -1
    return max_profit


print(maxDifference([7, 1, 2, 5]))
print(maxDifference([7, 5, 3, 1]))
# 1222 output expected
print(maxDifference([100, -129, 877, -166, 433, 547, 413, 311, 311, 307, 15, 334, -58, 821, 335, 646, 697, 845, -156,
                     781, -84, 675, 833, 182, 937, -246, 865, 603, 534, 912, 618, 494, -73, 131, 28, 282, 412, 489, 902,
                     842, 259, 844, 720, 324, -154, 757, 662, 628, -5, 163, 178, -7, -18, 365, 303, 530, 744, 838, 626,
                     -175, 216, 22, 976, 704, 782, 579, 151, 764, 494, -28, 699, 718, 351, 959, 407, 256, 215, 952, 328,
                     631, 228, 711, 438, 753, 830, 28, 81, 410, 621, 543, 745, 714, 829, 457, 481, 136, 134, 50, 678,
                     -235, 256]))
