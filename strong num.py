'''Strong number
Example
Input : 145
Output : It's a Strong Number.
Explanation : Number = 145
145 = 1! + 4! + 5!
145 = 1 + 24 + 120'''

#Using iteration
n=145
temp=n
sum=0
f=[0]*10
f[0]=1
f[1]=1
for i in range(2,10):
    f[i]=f[i-1]*i
while(temp):
    r=temp%10
    temp=temp//10
    sum+=f[r]
if (sum==n):
    print("Strong")
else:
    print("Not")
    
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
