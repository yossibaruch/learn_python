def loop_over_for(iterator, adder):
    numbers = []
    for i in range(0, iterator, adder):
        print("At the top, i is %d" % i)
        numbers.append(i)
        print("Numbers now:", numbers)
        print("At the bottom i is %d" % i)
    print("The Numbers: ")
    for num in numbers:
        print(num)


def loop_over(iterator, adder):
    i = 0
    numbers = []
    while i < iterator:
        print("At the top, i is %d" % i)
        numbers.append(i)
        i += adder
        print("Numbers now:", numbers)
        print("At the bottom i is %d" % i)
    print("The Numbers: ")
    for num in numbers:
        print(num)

loop_over(10, 2)
loop_over_for(10, 2)
