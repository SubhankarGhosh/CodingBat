def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    sub = str[i:i+2]
    if sub == "hi":
      count = count + 1
  return count