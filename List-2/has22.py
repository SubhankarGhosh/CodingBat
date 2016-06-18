def has22(nums):
  prev = 0
  cur = 0
  for i in range(len(nums)):
    cur = nums[i]
    if cur == prev and prev == 2:
      return True
    prev = cur
  return False
