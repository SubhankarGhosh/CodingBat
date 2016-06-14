def rotate_left3(nums):
  first = nums[0]
  for i in range(len(nums)-1):
    nums[i] = nums[i+1]
  nums[i+1] = first
  return nums
