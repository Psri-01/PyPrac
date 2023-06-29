def replacePi(input):
    output=' '
    size=len(input)
    for i in range(size):
        if(i+1<size and input[i]=='p' and input[i+1]=='i'):
            output += '3.14'
            i+=1
        else:
            output+=input[i];
    return output;
strin = "pippppxpiixipi" 
print(replacePi(strin))
