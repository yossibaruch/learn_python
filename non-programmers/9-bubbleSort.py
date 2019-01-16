print("""
# Get list of items
# Bubble sort the list:
#    - Iterate on all indices
#    - if adjacent items are out of order - swap them
#    - repeat n times (n is list length)
""")
array = []
while True:
    try:
        array = [int(x) for x in input().split()]
    except ValueError:
        print("This is not a list of integers, please make corrections")
        continue
    break

while not array == sorted(array):
    for i in range(len(array)-1):
        array[i], array[i+1] = (array[i], array[i+1]) if array[i] < array[i+1] else (array[i+1], array[i])

print(array)
