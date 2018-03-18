string1=input('')
string1=string1.casefold()
string2=reversed(string1)
if list(string1)==list(string2):
    print('yes')
else:
    print('no')

