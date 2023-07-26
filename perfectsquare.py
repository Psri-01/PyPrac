from math import sqrt
def isPerfectSquare(x):
    if x>=0:
        sr=int(sqrt(x))
        return sr*sr==x
    return False
n=64
if isPerfectSquare(n):
    print('True')
else:
    print('False')

# If floor and ceil function are equal it implies the number is a perfect square.
import math
def checkperfectsquare(n):
    if(math.ceil(math.sqrt(n))==math.floor(math.sqrt(n))):
        print('True')
    else:
        print('False')
checkperfectsquare(100)
