n = input('enter value: ')

s = int(n)*int(n)
a = ''
print('-'*50)
print(s)
print('-'*50)
for i in range(len(n)):
    d = s%10
    a = (str(d)+a)
    s = s//10
    print('value of a is',a)
else:
    if a == n:
        print('{} is a magic number'.format(n))
    else:
        print('{} not a magic number'.format(n))
