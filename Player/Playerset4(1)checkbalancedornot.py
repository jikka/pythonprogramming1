try:
  s=str(input())
  x1=0
  x2=0
  for i in range(s):
    if(s=='('):
      x1+=1
    elif(s==')'):
      x2+=1
  if(x1==x2):
    print('yes')
  else:
    print('no')
except:
  print('Invalid')  
