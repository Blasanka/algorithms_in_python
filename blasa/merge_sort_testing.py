values = []

for i in range(1,4):
    #values.append(input("Enter a number: ")) # <- for alphabet
    values.append(int(input("Enter a number: ")))

def mergeSort(arr):
    if len(arr)>1:
        middle = len(arr)//2
        leftPart = arr[:middle]
        rightPart = arr[middle:]

        mergeSort(leftPart)
        mergeSort(rightPart)

        i=0
        j=0
        k=0
        while i < len(leftPart) and j < len(rightPart):
            if leftPart[i] < rightPart[j]:
                arr[k]=leftPart[i]
                i=i+1
            else:
                arr[k]=rightPart[j]
                j=j+1
            k=k+1

        while i < len(leftPart):
            arr[k]=leftPart[i]
            i=i+1
            k=k+1

        while j < len(rightPart):
            arr[k]=rightPart[j]
            j=j+1
            k=k+1

print("Before sorting")
print(values)

print("After sorting")
mergeSort(values)
print (values)
