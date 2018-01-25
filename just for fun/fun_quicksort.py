def quicksort(A, lowerq, upperq):
    print(A, lowerq, upperq, "in quicksort")
    if lowerq < upperq:
        p = partition(A, lowerq, upperq)
        quicksort(A, lowerq, p - 1)
        quicksort(A, p + 1, upperq)
    return A


def partition(A, lowerp, upperp):
    print(A, lowerp, upperp, "in partition start")
    pivot = A[lowerp]
    index_l = lowerp + 1
    index_r = upperp
    done = False
    while not done:
        while (index_l <= index_r) and (A[index_l] <= pivot):
            index_l += 1
        while (index_l <= index_r) and (A[index_r] >= pivot):
            index_r -= 1
        if not (index_l > index_r):
            A[index_l], A[index_r] = A[index_r], A[index_l]
        else:
            done = True
    A[lowerp], A[index_r] = A[index_r], A[lowerp]
    return index_r


A = [5, 2, 3, 10, 1, 8, 6, 4, 7]
print(A, 0, len(A) - 1)
print(quicksort(A, 0, len(A) - 1))
