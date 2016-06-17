def make_chocolate(small, big, goal):
  if (goal > big*5) and (goal-(5*big) <= small):
    return goal-(5*big)
  elif (goal < big*5) and (goal%5 <= small):
    return goal%5
  elif goal == big*5:
    return 0
  elif goal == small:
    return small
  else:
    return -1