s = input('enter value: ')
a = s[-1:-(len(s)+1):-1]
print(a)

if s == a:
    print('{} is pallendrome'.format(s))
else:
    print('{} not a pallendrome'.format(s))

