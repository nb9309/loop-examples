lst = []
while 9:
    val = input('enter value: ')
    if val == '!':
        break
    lst.append(val)
print(lst)
lst1 = []
for i in lst:
    res = False
    if i == i[::-1]:
        res = True
    if res:
        lst1.append(i)
else:
    print('-'*50)
    print(lst1)