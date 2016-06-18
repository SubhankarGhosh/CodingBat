def xyz_there(str):
  for i in range(len(str)-2):
    sub = str[i:i+3]
    if (i==0 and sub=="xyz") or (sub=="xyz" and str[i-1]!="."):
      return True
  return False
