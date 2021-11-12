#1'den N'e kadar sayıların toplamını veren işlemin rekürsif hali
def topla(n):
  if n<=1:
    return 1
  else:
    return (n+topla(n-1))
