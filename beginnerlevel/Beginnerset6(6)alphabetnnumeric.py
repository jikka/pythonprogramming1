a=0
n=0
N=str(input())
print(a)
if(len(N<=1000)):
  for i in range(len(N)):
    if(N[i].isalpha()):
      a+=1
    elif (N[i].isnumeric()):
      n+=1
if(a+n==len(N) and a>0 and n>0):
  print('Yes')
else:
  print('No')
