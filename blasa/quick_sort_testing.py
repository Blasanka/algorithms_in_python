values = []

for i in range(1,4):
    #values.append(input("Enter a number: ")) # <- for alphabet
    values.append(int(input("Enter a number: ")))

def partition(arr, p, r):
    x = arr[r]
    i = p -1
    
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i+1]
    arr[i+1] = arr[r]
    arr[r] = temp
    return i + 1

def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q-1)
        quickSort(arr, q + 1, r)


print("Before sort")
print(values)

print("After sort")
quickSort(values, 0, len(values)-1)
print (values)
