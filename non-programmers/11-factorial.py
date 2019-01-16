print("""
# Get a number: n
# Calculate n!:
#     - multiply all numbers between n..1
""")


def factorial(Number):
    f = Number
    while not Number == 1:
        f *= Number - 1
        Number -= 1
    return f


def factorial_rec(Number):
    if Number == 0:
        return 1
    else:
        return Number * factorial_rec(Number-1)


while True:
    try:
        N = int(input("Please print a number N to calculate N! :"))
    except ValueError:
        print("this is not an integer, try again...")
        continue
    break

if N < 1:
    print("Messing with me, this number is smaller than 1!!!")
    exit(0)

print(factorial(N))
print(factorial_rec(N))
