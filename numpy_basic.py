'''You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.'''

import numpy
L = list(map(float,input().split()))
x = input();
print (numpy.polyval(L, int(x))) #The polyval tool evaluates the polynomial at specific value.

'''You are given a square matrix A with dimensions NxN. 
Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.'''
import numpy
N = int(input())
A = numpy.array([input().split() for _ in range(N)],float)
print(round(numpy.linalg.det(A),2))
#ALITER
import numpy
arr = []
for _ in range(int(input())):
    arr.append(list(map(float,input().split())))
out = numpy.linalg.det(numpy.array(arr))
#print("{0:.2f}".format(out))
print(round(out,2))

'''ARRAY(2 arrays A,B of dim N x M) MATH'''
import numpy
N, M = map(int, input().split())
A = numpy.array([list(map(int, input().split())) for n in range(N)])
B = numpy.array([list(map(int, input().split())) for n in range(N)])
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
