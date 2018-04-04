try:
  N=int(input())
	l=[]
	for i in range(N):
		l.append(int(input()))
	for i in range(1,N):
		if l[i-1]>l[i]:
			print(l[i-1])
			break
except:
	print('invalid')
