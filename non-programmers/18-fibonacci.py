from math import sqrt
import time
print("""
# Calculate fibonacci series in many ways
#   - Recursion
#   - Iterations
#   - Memoization
#   - Calculation
""")


def fib_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


def fib_ite(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_mem(n):
    if not hasattr(fib_mem, 'ret'):
        fib_mem.ret = [0, 1]
    if len(fib_mem.ret) < n:
        for _ in range(len(fib_mem.ret), n + 1):
            fib_mem.ret.append(fib_mem(_ - 1) + fib_mem(_ - 2))
    return fib_mem.ret[n]


def fib_calc(n):
    num1 = (1 + sqrt(5))/2
    num2 = (1 - sqrt(5))/2
    return round((num1**n - num2**n)/(sqrt(5)))


def calc_time(fun, n):
    start = time.time()
    answer = fun(n)
    end = time.time()
    return [answer, end - start]


N = 35
print(calc_time(fib_rec, N), calc_time(fib_ite, N), calc_time(fib_mem, N), calc_time(fib_calc, N))
