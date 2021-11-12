#1'den n'e kadar sayıların çarpımını veren işlemin rekürsif hali
def çarp(n):
  if n<=1:
    return 1
  else:
    return (n*çarp(n-1))
