"""
Find the number of 7-tuple of positive integers (a,b,c,d,e,f,g) that satisfy:
    a*b*c = 70
    c*d*e = 71
    e*f*g = 72
"""


def factor_of_num(number):
    number_factors = []
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
            number_factors.append(i)
    return count, number_factors


print(
    """
    please find the 7-tuple (a,b,c,d,e,f,g) that fits the criteria a*b*c = 70, c*d*e = 71, e*f*g = 72,
    It seems that c=e=1 and d=71 for the exercise to have a solution
    """
      )

numberOfSets = 0
testCriteria = [
    70,
    71,
    72
]
# for x in 0, 2:
#     y = factor_of_num(testCriteria[x])
#     print(y)
#     # for z in y[1]:
#     #     v = factor_of_num(z)
#     #print(v)

set1 = factor_of_num(testCriteria[0])
set2 = [
    1,
    71,
    1
]
set3 = factor_of_num(testCriteria[2])

# outcome = [i for i in set1[1] for j in set3[1]]


# for i, j in zip(set1[1], set3[1]):
#     print(i, j)

for x, y in [(x, y) for x in set1[1] for y in set3[1]]:
    print(x, int(testCriteria[0] / x), set2[0], set2[1], set2[2], y, int(testCriteria[2] / y))
    numberOfSets += 1

print("Number of possible sets is: ", numberOfSets)
