N=int(input())
pro=1
if(n<=100000000000):
  while(n>0):
    dig=n%10
    pro=pro*dig
print(pro)
