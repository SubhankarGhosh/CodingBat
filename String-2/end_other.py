def end_other(a, b):
  a = a.lower()
  b = b.lower()
  len_a = len(a)
  len_b = len(b)
  return a==b[-len_a:] or a[-len_b:]==b
    
