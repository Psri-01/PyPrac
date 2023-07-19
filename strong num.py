'''Strong number
Example
Input : 145
Output : It's a Strong Number.
Explanation : Number = 145
145 = 1! + 4! + 5!
145 = 1 + 24 + 120'''

#Using Recursion
def Factorial(num):
    if num<=0: return 1 else: return num*Factorial(num-1) sum=0 def check_StrongNumber(num): global sum if (num>0):
        fact = 1
        rem = num % 10
        check_StrongNumber(num // 10)
        fact = Factorial(rem)
        sum+=fact
    return sum
num=145
if (check_StrongNumber(num) == num):
    print("Yes",num,"is a strong Number.")
else:
    print("No",num,"is not a strong Number.")
