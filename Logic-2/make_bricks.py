def make_bricks(small, big, goal):
  if (goal > big*5) and (goal-(5*big) <= small):
    return True
  elif (goal < big*5) and (goal%5 <= small):
    return True
  elif goal == big*5 or goal == small:
    return True
  else:
    return False