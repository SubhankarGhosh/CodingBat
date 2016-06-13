def last2(str):
  if len(str) == 0:
    return 0
  sub = str[-2:]
  index = -1
  count = -1
  while index < len(str)-1:
    index = str.find(sub, index)
    if index is not -1:
      count = count + 1
    index = index + 1
  return count
