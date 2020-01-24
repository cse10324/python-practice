# module python code

# from math import sqrt

# print(sqrt(4))

# #defining it after the import statement will
# #overwrite the function with the same name
# def sqrt(param):
#     return param*100

# print(sqrt(4))

# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)