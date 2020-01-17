# Create a function named max_num() that 
# takes a list of numbers named nums as a parameter.

# The function should return the largest number in nums

def max_num(nums):
  maxNum = -99999999
  for count in range(len(nums)):
    if maxNum < nums[count]:
      maxNum = nums[count]
  return maxNum

print(max_num([50, -10, 0, 75, 20]))