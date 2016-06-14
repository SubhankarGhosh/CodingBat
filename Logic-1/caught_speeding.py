def caught_speeding(speed, is_birthday):
  if (is_birthday and speed<=65) or speed<=60:
    return 0
  elif (is_birthday and (speed>=66 and speed<=85)) or speed<=80:
    return 1
  else:
    return 2