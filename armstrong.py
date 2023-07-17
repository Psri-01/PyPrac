low, high=150,10000
for n in range(low,high+1):
    order=len(str(n))
    sum=0
    temp=n 
    while temp>0:
        digit=temp%10 
        sum+=digit**order
        temp//=10 
    if n==sum:
        print(n,end=" ")

number = 153
num=number
digit, sum= 0,0
length=len(str(num))
for i in range(length):
    digit=int(num%10)
    num=num/10
    sum+=pow(digit,length)
if sum==number:
    print('Armstrong')
else:
    print('Not arm')
