'''You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.'''

import numpy
L = list(map(float,input().split()))
x = input();
print (numpy.polyval(L, int(x))) #The polyval tool evaluates the polynomial at specific value.
