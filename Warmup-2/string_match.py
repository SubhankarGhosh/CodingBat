def string_match(a, b):
  lena = len(a)
  lenb = len(b)
  mini = min(lena, lenb)
  count = 0
  for i in range(mini-1):
    if a[i:i+2] == b[i:i+2]:
      count = count + 1
  return count
