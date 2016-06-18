def sum13(nums):
  sum = 0
  i = 0
  while i<len(nums):
    if nums[i]!=13:
      sum = sum + nums[i]
      i = i+1
    else:
      i = i+2
  return sum