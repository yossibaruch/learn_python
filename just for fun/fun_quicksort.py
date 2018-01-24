def quicksort(A, lowerq, upperq):
    # print(A, lowerq, upperq)
    if lowerq < upperq:
        p = partition(A, lowerq, upperq)
        quicksort(A, lowerq, p-1)
        quicksort(A, p+1, upperq)
    return A


def partition(A, lowerp, upperp):
    # print(A, lowerp, upperp)
    pivot = A[upperp]
    i = lowerp
    range
    print(q)
    for j in range(lowerp, upperp-1):
        if A[j] < pivot:
            i = i+1
            A[i], A[j] = A[j], A[i]
    if A[upperp] < A[i+1]:
        A[i+1], A[upperp] = A[upperp], A[i+1]
    return i+1


A = [1, 2, 9, 3, 7, 2, 3, 8, 2, 5]
lower = 0
upper = len(A)-1

print(A, lower, upper)
# print(A[lower], A[upper])

print(quicksort(A, lower, upper))


