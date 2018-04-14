def small2(l,K):
	l.sort()
	return l[K-1]
def main():
	try:
		N=int(input())
		K=int(input())
		l=[]
		for i in range(N):
			l.append(int(input()))
		print(small2(l,K))
	except:
		print('invalid')
main()
