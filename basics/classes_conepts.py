# Call type() on the integer 5 and print the results.
#print(type(5))

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

class Dog():
    dog_time_dilation = 7 
#methods inside class needs compulsory one paramter, the first argument in a method is always the object that is calling the method. Convention recommends that we name this first argument self.    
    def time_explanation(self):
        print("Dog experiences {} years for every 1 human year".format(self.dog_time_dilation))

# pipi_pitbull = Dog()
# pipi_pitbull.time_explanation()

class DistanceConverter:
    kms_in_a_mile = 1.609
    def how_many_kms(self, miles):
        return miles*self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
# print(kms_in_5_miles)

# CONSTRUCTORS IN PYTHON
# class Shouter:
#     def __init__(self):
#         print("HELLO!!!!")

#__init__ method is called every time class is instantiated, is also called as constructor
# one_call = Shouter()
# second_call = Shouter()

# pass the value to the constructor
class Shouter:
    def __init__(self, phrase):
        #make sure the phrase is a string
        if type(phrase) == str:
            #shout it
            print(phrase.upper())
        else:
            print("You sir has just entered a value other than a string")

one_call = Shouter("shout")
second_call = Shouter("let's hear it out")
#pass a integer as a parameter now
third_call = Shouter(4)    #this will not be printed

