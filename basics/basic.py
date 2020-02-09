# boolean operations example
# if(not True == True):
#     print("True")
# else:
#     print("False")

#join strings on a character
joinedStrings = "-".join(["Codecademy","is","awesome"])
#print(joinedStrings)

numbers = [0,254,2,-1,3]

for number in numbers:
    if number < 0:
        print("Negative number alert!")
        break
    else:
        print(number)
