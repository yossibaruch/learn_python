def add(a, b):
    print("adding", a, "+", b)
    return a + b


def subtract(a, b):
    print("substracting", a, "-", b)
    return a - b


def multiply(a, b):
    print("multiplying", a, "*", b)
    return a * b


def divide(a, b):
    print("dividing", a, "/", b)
    return a / b


def formula(a, b, c, d, e, f, g, h):
    return (a+b)+((c-d)-((e * f)*((g / h) / 2)))


print("Let's do some math with just functions!")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))
print("Here is a puzzle.")

what1 = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what2 = formula(30, 5, 78, 4, 90, 2, 100, 2)
print("That becomes: ", what1, "Can you do it by hand?")
print("That is: ", what2, "by formula")
