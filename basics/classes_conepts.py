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

# one_call = Shouter("shout")
# second_call = Shouter("let's hear it out")
# #pass a integer as a parameter now
# third_call = Shouter(4)    #this will not be printed

#print the paramter value passed through using .format() method
class Circle:
    def __init__(self,diameter):
        print("New circle with diameter: {}".format(diameter))

# teaching_table = Circle(36)

class Area:
    def __init__(self, radius):
        area = 2*3.14*radius
        return area

# __init__ cannot return any value, it can only return none or no value
# one_call = Area(12) #error: TypeError: __init__() should return None, not 'float'

class FakeDict:
    pass

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

#two instances created for different object of same class having same name "fake_key"
#can store any data type mostly
fake_dict1.fake_key = "This Works!!"
fake_dict2.fake_key = 8

#lets join the string together
working_string = "{}{}".format(fake_dict1.fake_key, fake_dict2.fake_key)

#print(working_string)

class SearchEngineEntity:
    secure_prefix = "https://"
    def __init__(self, url):
        self.url = url
    
    def secure_url(self):
        return "{prefix}{site}".format(prefix=self.secure_prefix,site=self.url)
    
codecademy = SearchEngineEntity("www.codecademy.com")
wikipedia = SearchEngineEntity("www.wikipedia.com")

# print(codecademy.secure_url())
# print(wikipedia.secure_url())

class Circle:
    pi = 3.14
    
    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
        self.radius = diameter/2
    
    def circumference(self):
        circumference = 2*self.pi*self.radius
        return circumference
    
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

