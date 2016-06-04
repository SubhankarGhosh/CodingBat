def array_front9(nums):
#  ind = nums.index(9)
#  return (ind<4 and ind>=0)
  for i in range(min(len(nums),4)):
    if nums[i] == 9:
      return True
  return False
