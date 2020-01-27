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
# try:
#     print(zodiac_elements["energy"])
# except KeyError as K:
#     print("Key " +str(K)+ " does not exist in the dictionary")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

#get the value of key without any error, NONE will be received in case of no value found
tc_id = user_ids.get("teraCoder",100000)
#print(tc_id)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# You are designing the video game Big Rock Adventure. We have provided a dictionary of items that are in the player’s inventory which add points to their health meter. In one line, add the corresponding value of the key "stamina grains" to the health_points variable and remove the item "stamina grains" from the dictionary. If the key does not exist, add 0 to health_points.

health_points += available_items.get("stamina grains",0)
available_items.pop("stamina grains",0)

# print(health_points)

# In one line, add the value of "power stew" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.
health_points += available_items.get("power stew",0)
available_items.pop("power stew",0)

# In one line, add the value of "mystic bread" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.
health_points += available_items.get('mystic bread',0)
available_items.pop("mystic bread",0)

# Print available_items and health_points.
# print(available_items)
# print(health_points)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Create a variable called users and assign it to be all of the keys of the user_ids list.
users = user_ids.keys()

# Create a variable called lessons and assign it to be all of the keys of the num_exercises list.
lessons = num_exercises.keys()

print(users)
# output: dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])
print(lessons)
# output: dict_keys(['functions', 'syntax', 'control flow', 'loops', 'lists', 'classes', 'dictionaries'])


