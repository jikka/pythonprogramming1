string=srt(input(' '))
if (1<=len.string<=100000):
  l=list(string.split(' '))
  s=' '
  for i in range(len(l)):
    s+=l[i][::-1]+' '
  print(string)
    
