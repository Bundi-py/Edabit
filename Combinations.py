# Create a function that takes a variable number of groups of items, and returns the number
# of ways the items can be arranged, with one item from each group. Order does not matter.
# Examples:
# combinations(2, 3) ➞ 6
# combinations(3, 7, 4) ➞ 84
# combinations(2, 3, 4, 5) ➞ 120
# Notes:
# Don't overthink this one.


def combinations(*items):
    res = 1
    for i in items:
        res *= i
    return items


combinations(2, 3, 4, 5)
