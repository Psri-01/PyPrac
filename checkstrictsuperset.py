'''Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.'''

a = set(input().split())
n = int(input()) #number of other sets
print(all(a>set(input().split())for _ in range(n)))
