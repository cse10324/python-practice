# module python code

from math import sqrt

print(sqrt(4))

#defining it after the import statement will
#overwrite the function with the same name
def sqrt(param):
    return param*100

print(sqrt(4))