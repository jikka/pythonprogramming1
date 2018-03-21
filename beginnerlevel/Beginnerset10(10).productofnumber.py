N=int(input())
product=1
if(N<=100000000000):
    while(N>0):
      dig=N%10
      N=N//10
      product=product*dig
print(product)
