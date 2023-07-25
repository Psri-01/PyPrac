import math
num=376
square=pow(num,2)
mod=pow(10, len(str(num)))
if square%mod==num:          #141376 % 1000
    print('Automorphic number')
else:
    print('Not an Automorphic number')

# One line method for automorphic number in python
n = 376
# n^2 = 141376 141376[-3::] = 376
print("yes" if int(str(n**2)[-len(str(n))::]) == n else "no")

#The endswith() method returns True if the string ends with the specified value, otherwise False.
num=376
a=str(num)
num1=num**2
b=str(num1)
if b.endswith(a):
    print('Automorphic')
else:
    print('No')
