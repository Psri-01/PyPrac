n1=12
n2=14
for i in range(max(n1,n2),1+(n1*n2)):
    if i%n1==i%n2==0:
        lcm=i
        break
print('LCM of',n1,'and',n2,'is',lcm)

n1=12
n2=14
for i in range(max(n1,n2),1+(n1*n2),max(n1,n2)):
    if i % n1 == i % n2 == 0:
        lcm=i
        break
print('LCM of',n1,'and',n2,'is',lcm)

n1=12
n2=14
for i in range(1,max(n1,n2)):
    if n1%i==0 and n2%i==0:
        hcf=i
lcm = (n1*n2)//hcf
print(lcm)

def getHCF(n1,n2):
    while n1!=n2:
        if n1>n2:
            n1-=n2
        else:
            n2-=n1
    return n1
n1=12
n2=14
hcf=getHCF(n1,n2)
lcm=(n1*n2)//hcf
print('LCM is',lcm,'and',hcf,'is the HCF')
