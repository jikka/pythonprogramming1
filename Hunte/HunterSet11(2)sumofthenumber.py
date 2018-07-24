N=int(input())
sum=0
if (1<=N<=100000):
  while(N>0):
    x=N%10
    sum+=x*x
    N=N//10
print(sum)
