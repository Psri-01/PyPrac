'''Example
Input : 6 28
Output : Yes, they are a friendly pair
Explanation : The factors of 6 and 28 except the numbers themselves are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
Now the sum of factors of both the numbers are 6 and 28 respectively. 
When we divide the sums with the numbers we get 1 and 1 respectively. 
As the ratio of both the number match, they are considered as a friendly pair.'''
def printDivisors(n,factors):
    i=1
    while i<=n:
        if(n%i==0):
            factors.append(i)
        i=i+1
    return sum(factors) - n
if __name__ == "__main__": 
  number1, number2 = 6, 28
  if int(printDivisors(number1, [])/number1) == int(printDivisors(number2, [])/number2):
    print("Friendly pair")
  else:
    print("Not a Friendly Pair")

def printDivisors(n, factors) :
     
    # Note that this loop runs till square root
    i = 1
    while i <= pow(n,0.5):
         
        if (n % i == 0) :
             
            # If divisors are equal, print only one
            if (n / i == i) :
                factors.append(i)
            else :
                # Otherwise print both
                factors.append(i)
                factors.append(int(n/i))
        i = i + 1
    return sum(factors) - n

if __name__ == "__main__": 
  number1, number2 = 6, 28
  if int(printDivisors(number1, [])/number1) == int(printDivisors(number2, [])/number2):
    print("Friendly pair")
  else:
    print("Not a Friendly Pair")
