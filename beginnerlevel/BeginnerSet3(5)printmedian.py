import statistics
N=int(input())
ls=[]
for x in range(1,N+1):
  number=int(input())
  ls.append(number)
print(statistics.median(ls))
