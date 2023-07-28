# function to convert binary to octal
def convert(num):
    octalDigit = 0
    count = 1
    i = 0
    pos = 0
    octalArray = [0] * 32
    while num != 0:
        digit = num % 10
        octalDigit += digit * pow(2, i)
        i += 1
        num //= 10
        # placing current octal-sum for 3 pair in array index position
        octalArray[pos] = octalDigit
        # whenever we have read next 3 digits
        # setting values to default
        # increasing pos so next values can be placed at next array index
        if count % 3 == 0:
            octalDigit = 0
            i = 0
            pos += 1
        count += 1
    # printing octal array in reverse order
    for j in range(pos, -1, -1):
        print(octalArray[j], end='')
binary = 1010
convert(binary)

num=int(input("Enter the octal value "))
temp=num
bin_val=0
deci_val=0
base1=1
base2=1
while(temp):
    digit=temp%10
    deci_val+=digit*base1
    base1*=8
    temp//=10
    while(deci_val):
        rem=deci_val%2
        bin_val+=rem*base2
        base2*=10
        deci_val//=2
print("The binary value of {} is {}".format(num,bin_val))

def convert(octal):
    print("Equivalent Binary Number: ", end="")
    for i in range(len(octal)):
        switcher = {
            0: "000",
            1: "001",
            2: "010",
            3: "011",
            4: "100",
            5: "101",
            6: "110",
            7: "111"
        }
        print(switcher.get(int(octal[i]), "Invalid Octal Number"), end="")
octal = list(input("Insert an octal number: "))
convert(octal)
