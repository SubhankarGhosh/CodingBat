def pos_neg(a, b, negative):
  return ((((a*b)<0) and negative==False) or (a<0 and b<0 and negative==True))
