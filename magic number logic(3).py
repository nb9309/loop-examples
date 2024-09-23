n = int(input('enter value:'))

if n < 0:
    print(f'{n} is not valid')
else:
    if str(n**2).endswith(str(n)):
        print(n*n)
        print(f'{n} is magic number')
    else:
        print(n*n)
        print(f'{n} is not a magic number')