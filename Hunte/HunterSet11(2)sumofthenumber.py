try:
  N=int(input())
  sum=0
  if x in (1<=N<=100000):
    while(N>0):
      x=N%10
      sum+=x
      N=N//10
  print(sum*sum)
except:
  print('Invalid')
