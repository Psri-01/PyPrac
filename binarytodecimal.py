'''While num is greater than zero
Store the unit place value of num to a variable (rem)
Calculate rem with base and add it to answer
Completely divide Num by 10 and multiply base with 2'''

num=10
binary=num
decimal=0
base=1
while num>0:
    rem=num%10
    decimal=decimal+rem*base
    num=num//10
    base=base*2
print(binary, decimal)
