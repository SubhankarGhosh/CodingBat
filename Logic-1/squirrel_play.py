def squirrel_play(temp, is_summer):
  return (temp>=60 and temp<=100 and is_summer) or (temp>=60 and temp<=90 and (not is_summer))
