try:
  n=10
  ls=[]
  for x in range(n):
    number=int(input())
    ls.append(number)
  print(min(ls))
except:
  print('invalid')
