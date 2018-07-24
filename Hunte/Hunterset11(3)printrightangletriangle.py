try:
  N=int(input())
  for i in range(1,N*1):
    if(i%2!=0):
      for j in range(i):
        print('1',end=' ')
    print()
except:
  print('invalid')      
