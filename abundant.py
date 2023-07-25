n=12      #as 12<1+2+3+4+6
sum=1
for i in range(2,n):
    if(n%i==0):
        sum=sum+i
if(sum>n):
    print(n,'is an Abundant number')
else:
    print('Nu')

import math
n = 12
sum=1 # 1 can divide any number 
i=2

while(i<=math.sqrt(n)): 
  if(n%i==0): 
#if number is divisible by i add the number 
    if(n//i==i): 
# if quotient is equal to divisor add only one of them 
      sum=sum+i 
    else: 
        sum=sum + i + n/i 
        i=i+1 
    if(sum>n):
        print(n,"is Abundant Number")
    else:
        print(n,"is not Abundant Number")
