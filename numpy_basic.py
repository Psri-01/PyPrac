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
