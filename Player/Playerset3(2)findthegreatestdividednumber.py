n=int(input())
k=int(input())
if(n<=100000 and k<=100000):
  while(n!=k):
    if(n>k):
      n-=k
    else:
      k-=n
  print(n)
