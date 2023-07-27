'''Initialize a empty array as binaryArray
while input number is greater then 0
Append 1 if unit digit of num is odd else append 0
Assign half the value of num to num
Print all the values of  binaryArray'''
def convertBinary(num):
    binaryArray = []
    while num>0:
        binaryArray.append(num%2)
        num = num//2
    for j in binaryArray:
        print(j, end="")
decimal_num = 21
convertBinary(decimal_num)

'''Initialize variables binary, i, rem and assign 0, 1, 0 respectively
While input number is greater then zero run he loop
rem equals to divisibility of input by 2
num equals to half of num
Add rem * i to binary
Multiply i by 10
return binary  '''
def convertBinary(num):
    binary = 0
    i, rem = 1, 0
    while num != 0:
        rem = num % 2
        num = num // 2
        binary += rem * i
        i *= 10
    return binary


decimal_num = 21
print("Binary of", decimal_num, "is : ", end="")
print(convertBinary(decimal_num))

n=8
print(bin(n)[2:])

'''Take the decimal number from the user and store it in variable say decimal.
Create an array say octal to store the octal representation of the given decimal number.
Run a loop until decimal is not equal to 0 i.e., (decimal !=0)
Inside the loop insert the remainder that achieved by dividing decimal from 8 i.e., (decimal%8)
Coming out from the loop print the octal array in reverse order.'''
decimal = 148
octal = []
while decimal > 0:
    r = decimal % 8
    octal.append(r)
    decimal = decimal // 8
for i in reversed(octal):
    print(i, end="")

num=int(input(“Enter the decimal number “))
sum=0
temp=num
base=1
while(temp):
digit=temp%8
sum+=digit*base
base*=10
temp//=8
print(“The octal value of {} is {}”.format(num,sum))

'''If the current remainder left >= 10
Must be replaced by (A – F)
Else if current remainder < 10
Must be replaced by (0- 9)'''
def convert(num):
    hexa = []
    while num != 0:
        rem = num % 16
        if rem < 10:
            hexa.append(chr(rem + 48))
        else:
            hexa.append(chr(rem + 55))
        num = num // 16
    hexa.reverse()
    return ''.join(hexa)
decimal = 2545
print("Hexadecimal :", convert(decimal))
