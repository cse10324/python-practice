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

#anothery way of printing the zipped data
#print("zipped drinks: ", list(zipped_drinks))
    
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {songs:playcounts for songs, playcounts in zip(songs,playcounts)}

print(plays)