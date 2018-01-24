def quicksort(A, lowerq, upperq):
    print(A, lowerq, upperq, "in quicksort")
    if lowerq < upperq:
        p = partition(A, lowerq, upperq)
        quicksort(A, lowerq, p - 1)
        quicksort(A, p + 1, upperq)
    return A


def partition(A, lowerp, upperp):
    print(A, lowerp, upperp, "in partition")
    pivot = A[lowerp]
    index_l = lowerp + 1
    index_r = upperp

    while index_l < index_r:
        while (A[index_l] < pivot) and (index_l <= index_r): index_l += 1
        while (A[index_r] > pivot) and (index_l <= index_r): index_r -= 1
        A[index_l], A[index_r] = A[index_r], A[index_l]
        print(A, index_l, index_r, "in partition in while")
    A[lowerp], A[index_l] = A[index_l], A[lowerp]
    print(A, index_l, index_r, "in partition end")
    return index_r


A = [5, 2, 3, 10, 1, 8, 6, 4, 7]

print(A, 0, len(A) - 1)
# print(A[lower], A[upper])

print(quicksort(A, 0, len(A) - 1))
