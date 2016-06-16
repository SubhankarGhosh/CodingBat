def round10(num):
  unit = num % 10
  num = num/10
  if unit >= 5:
    num = num*10 + 10
  else:
    num = num * 10
  return num

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
