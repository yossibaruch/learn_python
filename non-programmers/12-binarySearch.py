import time
start_time = time.time()

print("""
# Get list and item to search
# If list is empty - return false
# If middle of list is item - return True
# If middle is bigger than item - perform search for left of list
# If middle is smaller than item - perform search for right of list
""")


def search_left(arr, index):
    print(arr, index, "search LEFT")
    return arr[0:index]


def search_right(arr, index):
    print(arr, index, "search RIGHT")
    return arr[index:len(arr)]


array = []
while True:
    try:
        array = [int(x) for x in input("Please input a list of integers").split()]
    except ValueError:
        print("This is not a list of integers, please make corrections")
        continue
    break

if not array:
    print("Array is empty")
    exit(False)

while True:
    try:
        item2Search = int(input("Which item do you seek?"))
    except ValueError:
        print("This is not an integer...")
        continue
    break

array = sorted(array)

while True:
    index = len(array) // 2
    if len(array) % 2 == 1 and item2Search == array[index]:
        print("Item found")
        print(array)
        print("--- %s seconds ---" % (time.time() - start_time))
        exit(True)
    else:
        array = search_right(array, index) if item2Search >= array[index] else search_left(array, index)
    if len(array) == 1 and item2Search != array[0]:
        print("Item not found")
        print("--- %s seconds ---" % (time.time() - start_time))
        exit(False)

