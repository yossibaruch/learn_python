def quicksort(A, lowerq, upperq):
    print(A, lowerq, upperq, "in quicksort")
    if lowerq < upperq:
        p = partition(A, lowerq, upperq)
        quicksort(A, lowerq, p-1)
        quicksort(A, p+1, upperq)
    return A



def partition(A, lowerp, upperp):
    print(A, lowerp, upperp, "in partition")
    pivot = A[lowerp]
    left = lowerp+1
    right = upperp
    for j in range(left, right):
        if A[j] > pivot:
            left = left+1
            A[left], A[j] = A[j], A[left]
    if A[upperp] < A[i+1]:
        A[i+1], A[upperp] = A[upperp], A[i+1]
    return i+1


A = [1, 2, 9, 3, 7, 4, 10, 8, 6, 5]

print(A, 0, len(A)-1)
# print(A[lower], A[upper])

print(quicksort(A, 0, len(A)-1))


