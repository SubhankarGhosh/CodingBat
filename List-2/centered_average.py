def centered_average(nums):
  maxi = max(nums)
  mini = min(nums)
  sum_lst = sum(nums)
  avg = (sum_lst - maxi - mini)/((len(nums))-2)
  return avg
