# https://projecteuler.net/problem=458
import math
from itertools import permutations


perm_project = permutations(['p', 'r', 'o', 'j', 'e', 'c', 't']).join('')

newlist = [x.join('') for x in list(perm_project)]

print(newlist)
