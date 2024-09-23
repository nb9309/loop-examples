lst = []
while 9:
    val = input('enter value: ')
    if val == '!':
        break
    lst.append(val)
print(lst)
d = {}
for word in lst:
    d[word] = len(word)
else:
    a = max(d.values())
    for w,wl in d.items():
        if wl == a:
            print("'{}' is a highest word".format(w))

