 def findrepeat(li):
	li.sort()
	rep=[]
	=len(li)
	for i in range(1,n):
			if li[i]==li[i-1] :
				if li[i] in rep :
					continue
				rep.append(li[i])
	print(rep)

def main():
	try:
		li=[]
		=int(input())
		for i in range(N):
			li.append(int(input()))
		findrepeat(li)
	except:
		print('invalid')

main()
