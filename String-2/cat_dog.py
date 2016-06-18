def cat_dog(str):
  count = 0
  for i in range(len(str)-2):
    sub = str[i:i+3]
    if sub == "cat":
      count = count + 1
  for i in range(len(str)-2):
    sub = str[i:i+3]
    if sub == "dog":
      count = count - 1
  return count==0