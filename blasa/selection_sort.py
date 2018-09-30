#desc(problem with minus)

def selectionSort(A):
    for j in range(len(A)):
        min = j
        for i in range(j+1,len(A)):
            if A[min] > A[i]:
                min = i
            temp = A[i]
            A[i] = A[min]
            A[min] = temp


arr = [1, 9, 3, 7]
selectionSort(arr)
print("in descending order")
print(arr)
