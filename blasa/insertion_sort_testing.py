userInputs = []

for i in range(1,4):
    userInputs.append(input("Enter a number between 10 to 20: "))

print("before apply sorting")
print(userInputs)

def insertionSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j -1
        #while(i >= 0 and arr[i] > key):
        #above line is failing for integer according to lab session
        #the best approch for integer is as follows
        while(i >= 0 and int(arr[i]) > int(key)):# <- what I found out
            arr[i+1] = arr[i]
            i = i -1
        arr[i + 1] = key

insertionSort(userInputs)
print(userInputs)



