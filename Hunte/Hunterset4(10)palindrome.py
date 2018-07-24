try:
  N=int(input())
  s=0
  tmp=N
  if(2<=N<=1000000000000000000):
    while(N>0):
      rem=N%10
      s=s*10+rem
      N=int(N/10)
  if s==tmp:
    print('yes')
  else:
    print('no')
except:
  print('Invalid')
