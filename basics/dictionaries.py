names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

#make a dictionary using list comprehensions
students = {key:value for key,value in zip(names,heights)}
#print(students)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks= zip(drinks,caffeine)

#printing values from a zip object
# for value in zipped_drinks:
#     print(value)


    
