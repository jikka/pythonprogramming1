Try:
  N=int(input())
  ls=[]
  if (1<=N<=100000):
    for i in range(N):
      ls.append(int(input()))
  for i in range (N):
    for j in range(i+1,N):
      if (ls[i]==ls[j]):
        print(ls[i])
      else:
        print('Unique')
except:
  print('Invalid')
  
    
  
