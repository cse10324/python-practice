# module python code

# from math import sqrt

# print(sqrt(4))

# #defining it after the import statement will
# #overwrite the function with the same name
# def sqrt(param):
#     return param*100

# print(sqrt(4))

#Decimal datatype implmenetation

# # Import Decimal below:
# from decimal import Decimal

# # Fix the floating point math below:
# two_decimal_points = Decimal('0.2') + Decimal('0.69')
# print(two_decimal_points)

# four_decimal_points = Decimal('0.53') * Decimal('0.65')
# print(four_decimal_points)

# With an integer.
print(Decimal("10.5") + 3) # 13.5

# With a float.
# This will give an error
# NameError: name 'Decimal' is not defined
print(Decimal("10.5") + 3.0)

# Instead, just use the Decimal object for float values.
print(Decimal("10.5") + Decimal("3.0")) # 13.5