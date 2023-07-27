a=54
b=24
x=1
for i in range(1,min(a+1,b+1)):
    if a%i==0 and b%i==0:
        hcf=i
print("Hcf of",a,"and",b,"is",hcf)

n1=36
n2=60
a=n1
b=n2
while n1!=n2:
    if n1>n2:
        n1-=n2
    else:
        n2-=n1
print("Hcf of",a,"and",b,"is",n1)

def getHcf(a,b):
    return b==0 and a or getHcf(b,a%b)
num1=36
num2=60
print("Hcf of", num1, "and", num2, "is", getHcf(num1, num2))

n1=36
n2=60
gcd=1
for i in range(1,min(n1,n2)):
    if n1%i==0 and n2%i==0:
        gcd=i
print(gcd)
