# Create a function named reversed_list() that takes 
# two lists of the same size as parameters named lst1 and lst2.

# The function should return True if lst1 is the same as lst2 reversed. 
# The function should return False otherwise.

# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

def reversed_list(lst1,lst2):
    if(len(lst1) != len(lst2)):
        return "List size not equal"
    else:
        for count in range(len(lst1)):
            if(lst1[count] != lst2[len(lst2) - 1 - count]):
                return False
        return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
        