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

# # With an integer.
# print(Decimal("10.5") + 3) # 13.5

# # With a float.
# # This will give an error
# # NameError: name 'Decimal' is not defined
# print(Decimal("10.5") + 3.0)

# # Instead, just use the Decimal object for float values.
# print(Decimal("10.5") + Decimal("3.0")) # 13.5

from datetime import datetime

#creating an object of datetime, obj = datetime(YYYY, MM, DD, HH, MM, SS)
birthday = datetime(1993, 4, 29, 18, 52, 23)

# #print year
# print(birthday.year)

# #print month
# print(birthday.month)

# #print day
# print(birthday.day)

# #print weekday
# #0 for monday, 6 for sunday
# print(birthday.weekday())

#print(datetime.now())

#Get the difference between current time and previous any time
#only subtraction operation can be performed
#print(datetime.now() - datetime(2018, 4, 29))

date_converted = datetime.strptime('Jan 15, 2019','%b %d, %Y')
print(date_converted.month)
print(date_converted.year)