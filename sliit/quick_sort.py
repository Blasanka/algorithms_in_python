def partition(A, low, high):
    pivot = A[high]
    i = low -1
    for j in range(low, high):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], arr[i + 1]
    return i + 1


def quickSort(A, low, high):
    if low < high:
        q = partition(A, low, high)
        quickSort(A, low, q-1)
        quickSort(A, q+1, high)

arr = [20,51,11,1]
quickSort(arr, 0, len(arr)-1)
print(arr)
