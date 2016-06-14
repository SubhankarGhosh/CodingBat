def alarm_clock(day, vacation):
  if (day == 0 or day == 6) and vacation == True:
    return 'off'
  elif day == 0 or day == 6 or vacation == True:
    return '10:00'
  return '7:00'
