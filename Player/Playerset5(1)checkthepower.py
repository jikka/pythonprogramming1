def power():
  N=int(input())
  K=int(input())
  i=N
  while(i>1):
    i=N%K
    N//=2
  print(i==0)
power()
  
