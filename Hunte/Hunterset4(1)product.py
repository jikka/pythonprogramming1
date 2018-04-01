try:
  N=int(input())
  pro=1
  if(N<=100000):
    for i in range (N):
      number=int(input())
      pro=pro*number
    print(pro)
except:
  print('invalid')
