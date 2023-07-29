from itertools import permutations
seq=permutations(['1','2','3'])
print(seq)
for p in seq:
    print(p)

from itertools import permutations
seq=permutations(['A','B'])
for p in seq:
    print(p)

from itertools import permutations
list1=['1','2','3','4']
seq=permutations(list1)
for p in seq:
    print(p)

def factorial(num):
    fact=1
    for i in range(num,1,-1):
        fact*=i
    return fact
n=10
r=6
p=factorial(n)//factorial(n-r)
print(p)

import math
n = int(input(“Enter the number of Students:”))
m = int(input(“Enter the number of Seats:”))
print(math.perm(n, m))
