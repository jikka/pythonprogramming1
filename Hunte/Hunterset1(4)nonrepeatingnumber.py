Try:
  N=int(input())
  ls=[]
  c=0
  for i in range(N):
    ls.Append(int(input()))
  for i in range(N):
    for j in range(i+1,N):
      if(ls[i]==ls[j]):
        c+=1
        continue
      elif(c==0):
        print(ls[i])
except:
  print('Invalid')
      
