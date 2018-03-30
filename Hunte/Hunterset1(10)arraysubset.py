Try:
  N =int(input())
  M=int(input())
  A,B=[],[]
  f=0
  if(1<=N<=100000):
    for i in range(N):
      A.append(int(intput()))
    for i in range(M):
      B.append(int(input()))
    for j in B:
      if j in A:
        continue
      else:
        f=1
        break
  if(f==1)
    print('NO')
  else:
    print('YES')
except:
  print('Invalid')
