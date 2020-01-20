# Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.

# The letters in the returned list should be unique. For example,

# common_letters("banana", "cream")
# should return ['a'].

def common_letters(string_one,string_two):
  length_string_one = len(string_one)
  length_string_two = len(string_two)
  final_common = []
  if length_string_one < length_string_two:
    for count in range(len(string_one)):
      if (string_one[count] in string_two) and (string_one[count] not in final_common):
        final_common.append(string_one[count])
  return final_common
