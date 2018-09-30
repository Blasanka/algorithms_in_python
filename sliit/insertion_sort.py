
#lab session-------------------

A = []

for v in range(10):
    A.append(input('Enter a number: '))

print('\nunsorted array')
print (A)

def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1

        while(i >= 0 and A[i] > key):
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

insertionSort(A)

print('\nsorted array')
print(A)

print('\nsorted array elemenet by element')
for i in range(len(A)):
    print(A[i])
