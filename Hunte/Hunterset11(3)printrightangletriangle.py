try:
  N=int(input())
  for i in range(1,N+1):
    for j in range(i):
      print('1',end=' ')
    print()
expect:
  print('invalid')
      
