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

'''FLOOR CEIL AND RINT FUNCTIONS'''
import numpy as np
np.set_printoptions(legacy='1.13')
arr=np.array([float(i)for i in input().split()])
print(np.floor(arr),np.ceil(arr),np.rint(arr), sep="\n")

'''Sum and Product'''
import numpy
N,M = map(int,input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.prod(numpy.sum(A,axis=0),axis=0))

'''MIN & MAX'''
import numpy
N,M = map(int,input().split())
A = numpy.array([input().split()for _ in range(N)],int)
print(numpy.max(numpy.min(A,axis=1),axis=0))

'''MEAN, VAR, STD'''
import numpy
N,M = map(int,input().split())
A = numpy.array([list(map(int,input().split())) for _ in range(N)])
print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
print(numpy.round(numpy.std(A), 11))

'''DOT AND CROSS'''
import numpy
N= int(input())
A = numpy.array([input().split() for _ in range(N)],int)
B = numpy.array([input().split() for _ in range(N)],int)
print(numpy.dot(A,B))
print(numpy.cross(A,B))

'''INNER AND OUTER'''
import numpy
A = numpy.array(input().split(),int)
B = numpy.array(input().split(),int)
print(numpy.inner(A,B),numpy.outer(A,B),sep='\n')
