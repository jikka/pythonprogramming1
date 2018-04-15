try:
  N=int(input())
  sum=0
  if(1<=N<=100000):
    for x in range(N):
      Number=int(input())
      sum+=Number
  print(sum)
except:
  print('invalid')
