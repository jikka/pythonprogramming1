try:
  x=int(input())
  hr=int(x/60)
  min=x%60
  print(hr,min)
except:
  print('invalid')
