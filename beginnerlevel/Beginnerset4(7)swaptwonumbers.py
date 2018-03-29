a=int(input())
b=int(input())
temp=0
if (a<=100000 and b<=100000):
  temp=a
  a=b
  b=temp
  print(a,b)
  
