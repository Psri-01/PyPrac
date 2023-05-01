'''triangle pyramid'''
for i in range(1,int(input())+1): 
    print(((10**i-1)//9)**2)
    
"""
ABC is a right angled triangle.
∠ABC = 90 degree.
Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC. 
Your task is to find ∠MBC in degrees.
Input Format
The first line contains the length of side AB.
The second line contains the length of side BC.
Output Format
Output ∠MBC in degrees. 
Note: Round the angle to the nearest integer.
Sample Input
10
10
Sample Output
45°
"""
import math
ab,bc = int(input()),int(input())
print(str(round((math.degrees(math.atan2(ab,bc)))))+'°')

"""
Task 
You are given a complex z.Your task is to convert it to polar coordinates.
Input Format
A single line containing the complex number z. Note: complex() function can be used in 
python to convert the input as a complex number.
Output Format
Output two lines: 
The first line should contain the value of r. 
The second line should contain the value of θ.
Sample Input
1+2j
Sample Output
2.23606797749979 
1.1071487177940904
"""
from cmath import phase
z = complex(input())
print(abs(complex(z.real,z.imag)))
print(phase(complex(z.real,z.imag)))
