a = [3, 7, 4, 1, 8]

for index in range(1,len(a)):
    current = a[index]
    i = index

    while i>0 and a[i-1] > current:
        a[i] = a[i-1]
        i = i -1

    a[i] = current



print(a)
