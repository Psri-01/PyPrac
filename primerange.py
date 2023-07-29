low,high=2,12
primes=[2]
for num in range(low,high+1):
    flag=0 
    if num<2:
        flag=1 
    if num%2==0:
        continue
    iter=2
    while iter < int(num/2):
        if num%iter==0:
            flag=1 
            break
        iter+=1 
    if flag==0:
        primes.append(num)
print(primes)

def checkPrime(num):
    #  0, 1 and negative numbers are not prime
    if num < 2:
        return 0
    else:
        # no need to run loop till num-1 as for any number x the numbers in
        # the range(num/2 + 1, num) won't be divisible anyway
        # Example 36 won't be divisible by anything b/w 19-35
        x = num // 2
        for j in range(2, x + 1):
            if num % j == 0:
                return 0
    # the number would be prime if we reach here
    return 1
for i in range(1, 100 + 1):
    if checkPrime(i):
        print(i, end=" ")
