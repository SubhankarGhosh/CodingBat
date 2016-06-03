def string_bits(str):
  c=0
  newstr = ""
  for char in str:
    if c % 2 == 0:
      newstr = newstr + char
    c = c + 1
  return newstr
