try:
  N=int(input())
  ls=[]
  for i in range(0,N):
    ch=input()
    ls.append(ch)
  ls.sort(key=str.lower)
  print(ls)
except:
  print('invalid')
  
