l=int(input())
r=int(input())
count=0
if(l<=r<=100000):
  for num in range(l,r):
    if num > 1:
      for i in range(2,num):
        if (num % i) == 0:
          count+=1
          break
print(count)
    
          
