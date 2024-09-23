n = int(input('enter value:'))

if n <= 0:
    print('{} is invalid'.format(n))
else:
    for i in range(1,n):
        sum = 0
        for j in range(1,i//2+1):
            if i%j == 0:
                sum += j
        if sum == i:
            print(i,end=' ')