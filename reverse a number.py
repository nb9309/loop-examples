n =int(input('enter value: '))
if n <= 0:
    print('{} is invalid'.format(n))
else:
    tv = n
    rev_num = 0
    while tv > 0:
        d = tv % 10
        rev_num = rev_num*10 + d
        tv = tv//10

    if n == rev_num:
        print('{} is palendrome'.format(n))
    else:
        print('{} not a palendrome'.format(n))

