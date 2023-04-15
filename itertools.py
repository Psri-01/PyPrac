"""
You are given a function f(X) = X**2. You are also given K lists. The ith list consists 
of N elements. You have to pick one element from each list so that the value from the equation below 
is maximized: 
S = (f(X1) + f(X2) + ... + f(X(k)))%M
X(i) denotes the element picked from the ith list . Find the maximized value S(max) obtained.
Note that you need to take exactly one element from each list, not necessarily the largest 
element. You add the squares of the chosen elements and perform the modulo operation. 
The maximum value that you can obtain, will be the answer to the problem.
Input Format
The first line contains 2 space separated integers K and M. 
The next K lines each contains an integer N(i), denoting the number of elements in the ith list, 
followed by N(i) space separated integers denoting the elements in the list.
Output Format
Output a single integer denoting the value S(max).
Sample Input
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output
206
"""
from itertools import product
k,m = map(int,input().split())
arr = (list(map(int, input().split()))[1:] for _ in range(k))
print(max(map(lambda x: sum(i**2 for i in x)%m, product(*arr))))

'''PRODUCT'''
from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*list(product(a,b)))

'''PERMUTATIONS'''
from itertools import permutations
s,k = input().split()
result = list(permutations(s,int(k)))
for i in sorted(result):
    for x in i:
        print(x,end='')
    print()

'''COMBINATIONS'''
from itertools import combinations
s, k = input().split()
for i in range(1,int(k)+1):
    for j in combinations(sorted(s),i):
        print(''.join(j))

'''COMBINATIONS WITH REPLACEMENT'''
from itertools import combinations_with_replacement
s,k = input().split()
for i in combinations_with_replacement(sorted(s),int(k)):
    print("".join(i))

'''COMPRESS THE STRING'''
from itertools import groupby
s = input()
print(*[(len(list(g)),int(k))for k,g in groupby(s)])

'''You are given a list of N lowercase English letters. For a given integer K, you can select any 
K indices (assume 1-based indexing) with a uniform probability from the list.
Find the probability that at least one of the K indices selected will contain the letter: 'a'.
Input Format
The input consists of three lines. The first line contains the integer N, denoting the length 
of the list. The next line consists of N space-separated lowercase English letters, 
denoting the elements of the list.
The third and the last line of input contains the integer K, denoting the number of indices 
to be selected.
Output Format
Output a single line consisting of the probability that at least one of the K indices selected 
contains the letter:'a'.
Note: The answer must be correct up to 3 decimal places.
Sample Input
4 
a a c d
2
Sample Output
0.8333
'''
from itertools import combinations
input()
arr,k = input().split(),int(input())
l = list(combinations(arr,k))
print("%.4f" % (len(list(filter(lambda x: 'a' in x , l)))/len(l)))
