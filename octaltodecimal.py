octal_num=512
decimal_value=int(str(octal_num),8)
print(octal_num,decimal_value)

num=512
temp=num
deci=0
base=1
while(temp):
    digit=temp%10
    deci+=digit*base
    base=base*8
    temp//=10
print(num,deci)
