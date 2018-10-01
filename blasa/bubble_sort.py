arr = []

for i in range(1,4):
    arr.append(int(input("Enter a number: ")))

def bubbleSort(array):
    arrSize =len(array)
    for i in range(arrSize-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

print("Before sort")
print(arr)

print("After sort")
bubbleSort(arr)
print(arr)
