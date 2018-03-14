num=int(input())
if(num>1):
  for x in range(2,num):
    if(num//x==0):
      print('yes')
    else:
      print('no')
      
