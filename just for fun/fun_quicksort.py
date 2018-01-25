def get_list_of_int():
    return [int(x) for x in input("Please input the integers list with spaces in between, Enter to finish\n\n").split()]


def quicksort(list_of_int, lowerq, upperq):
    if lowerq < upperq:
        p = partition(list_of_int, lowerq, upperq)
        quicksort(list_of_int, lowerq, p - 1)
        quicksort(list_of_int, p + 1, upperq)
    return list_of_int


def partition(list_of_int, lowerp, right):
    pivot = list_of_int[lowerp]
    left = lowerp + 1
    done = False
    while not done:
        while (left <= right) and (list_of_int[left] <= pivot):
            left += 1
        while (left <= right) and (list_of_int[right] >= pivot):
            right -= 1
        if not (left > right):
            list_of_int[left], list_of_int[right] = list_of_int[right], list_of_int[left]
        else:
            done = True
            list_of_int[lowerp], list_of_int[right] = list_of_int[right], list_of_int[lowerp]
    return right


A = get_list_of_int()
print(quicksort(A, 0, len(A) - 1))
