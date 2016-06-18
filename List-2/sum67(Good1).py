def sum67(nums):
  sum = 0
  flag = 0
  for i in range(len(nums)):
    if nums[i]==6:
      flag = 1
    if flag==1 and nums[i]==7:
      flag=0
      continue
    if flag==0:
      sum = sum + nums[i]
  return sum
