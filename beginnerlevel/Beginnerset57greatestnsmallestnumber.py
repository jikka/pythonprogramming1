lis=[]
num=int(input())
if(num<=10000):
  for x in range(num):
    numbers=int(input())
    lis.append(numbers)
  print(max(lis))
  print(min(lis))
