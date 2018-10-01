userInputs = []

for i in range(1,4):
    userInputs.append(input("Enter a number between 10 to 20: "))

print("before apply sorting")
print(userInputs)

def insertionSort(arr):
    for j in range(1, len(arr)):
        current = arr[j]
        pos = j -1
        #while(i >= 0 and arr[i] > key):
        #above line is failing for integer according to lab session
        #the best approch for integer is as follows
        while(pos >= 0 and int(arr[pos]) > int(current)):# <- what I found out
            arr[pos+1] = arr[pos]
            pos = pos -1
        arr[i + 1] = current

insertionSort(userInputs)
print(userInputs)



