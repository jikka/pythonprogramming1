num=int(input())
rev=0
if(num<=1000):
  while(num>0):
    r=num%10
    rev=rev*10+r
    num=num//10
print(rev)
