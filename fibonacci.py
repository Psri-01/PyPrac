num=10
n1,n2=0,1
print('Fibonacci series: ',n1,n2,end=" ")
for i in range(2, num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3, end=" ")
print()

def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))
num=10
if num <=0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
for i in range(num):
    print(fibonacciSeries(i), end=" ")

'''direct formula to find nth term of Fibonacci Series as –
Fn = {[(√5 + 1)/2] ^ n} / √5'''
import math
def fibonacci(phi, n):
    for i in range(0,n+1):
        result=round(pow(phi,i)/math.sqrt(5))
        print(result,end=' ')
num=10
phi=(1+math.sqrt(5))/2
fibonacci(phi,num)
