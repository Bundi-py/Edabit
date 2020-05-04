# Create a function that takes numbers as arguments, adds them together, and returns the product of digits until the answer is only 1 digit long.
# Examples

# sum_dig_prod(16, 28) ➞ 6
# # 16 + 28 = 44
# # 4 * 4 =  16
# # 1 * 6 = 6

# sum_dig_prod(0) ➞ 0
# sum_dig_prod(1, 2, 3, 4, 5, 6) ➞ 2

# Notes
# The input of the function is at least one number.


def sum_dig_prod(*args):
    suma = sum(args)
    while suma > 9:
        prod = 1
        for i in str(suma):
            prod *= int(i)
        suma = prod
    return prod


print(sum_dig_prod(1, 2, 3, 4, 5, 6))
