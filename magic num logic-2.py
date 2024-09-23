n = input('enter value: ')
s = str(int(n)*int(n))
if n == s[-len(n):]:
    print('{} is magic number'.format(n))
else:
    print('{} not a magic number'.format(n))
