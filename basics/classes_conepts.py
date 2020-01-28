# Call type() on the integer 5 and print the results.
print(type(5))

my_dict={}
#Print out the type() of my_dict.
# print(type(my_dict))

my_list = []
#Print out the type() of my_list.
# print(type(my_list))

#output
# <class 'int'>
# <class 'dict'>
# <class 'list'>

#this will work
#pass keyword is used to indicate that, body of the class is intentionally left blank
#else it will cause error: SyntaxError: unexpected EOF while parsing
class CoolClass:
    pass

#here we are creating an instance of class, obly declaring class is of no use, we have to make use of it by creating an instance of that class
cool_instance = CoolClass()


