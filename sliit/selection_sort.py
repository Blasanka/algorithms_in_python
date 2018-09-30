def selectionSort(A):
    for j in range(len(A)):
        min = j
        for i in range(j+1,len(A)):
            if A[min] > A[i]:
                min = i
        temp = A[j]
        A[j] = A[min]
        A[min] = temp


arr = [1, -9, -555, 7]
selectionSort(arr)
print(arr)
