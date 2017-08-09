#-*-coding:utf-8-*-
def Permutation(self,a,b):
  m=list(a)
  n=list(b)
  m.sort()
  n.sort()
  if m==n:
    return True
  else:
    return False
  
