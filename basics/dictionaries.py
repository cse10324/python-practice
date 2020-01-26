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

# print(plays)

plays.update({"Respect":{"album 1": "123 time played","album 2":"1231 time played", "album 3":"12311 time played"}})

#print(plays)

#print the value associated with the key in dictionary
# print(plays["Respect"])

#try to access key which does not exist, should not throw error

# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

# zodiac_elements.update({"energy":"Not a Zodiac element"})

# key_to_check = "Landmark 81"

# if key_to_check in zodiac_elements:
#   print(zodiac_elements["Landmark 81"])

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

key_to_check = "energy"

#check if a key is present or not, will not throw error if not present
# if key_to_check in zodiac_elements:
#     print(zodiac_elements["energy"])

#Handle the non-exist key in the dictionary using the except block
try:
    print(zodiac_elements["energy"])
except KeyError as K:
    print("Key " +str(K)+ " does not exist in the dictionary")