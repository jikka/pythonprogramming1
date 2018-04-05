try:
  N=int(input())
  l=[]
  if(1<=N<=1000):
    for i in range(1,N//2+1):
      if N%i==0 and i%2==0:
        l.append(i)
	l.append(N)
  print(*l)
except:
  print('Invalid')
