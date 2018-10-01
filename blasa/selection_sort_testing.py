values = []

for i in range(1,4):
    values.append(int(input("Enter a number: ")))

def selectionSort(arr):
    size = len(arr)

    for j in range(0, size-1):
        smallest = j

        for i in range(j+1, size):
            if arr[i] < arr[smallest]:
                smallest = i

        temp = arr[j]
        arr[j] = arr[smallest]
        arr[smallest] = temp;


print("\nBefore sorting list")
print(values)

print("\nAfter sorting list")
selectionSort(values)
print(values)


print("\nElement by element")
for i in values:
    print(i)
