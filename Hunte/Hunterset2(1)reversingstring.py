def reverse():
	s=str(input())
	l=list(s.split())
	r=[]
	s=''
	for i in range(len(l)):
		s+=l[i][::-1]+' '
	print(s)
try:
  reverse()
except:
	print('invalid')
