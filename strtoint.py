def atoi(inputString):
    outputNum=0
    for char in inputString:
        for i in range(10):
            if str(i)==char:
                outputNum=outputNum*10+i
    return outputNum
x="123"
print(atoi(x))
