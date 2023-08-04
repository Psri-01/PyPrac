def double_word(word):
  return str(word*2)+str(len(word)*2)
print(double_word("hello"))
print(double_word("abc"))
print(double_word(""))

exp = "(a-b)+[c*d]+{e/f}"
equation = ''
for i in exp:
    if ord(i)==41 or ord(i)==40 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125:
        pass
    else:
        equation=equation+i
print(equation)

string="daya124829abh0"
sum1=0
for i in string:
    if ord(i)>=48 and ord(i)<=57:
        sum1=sum1+int(i)
print(str(sum1))
#ALITER
import re
def find_sum(str1):
    return sum(map(int, re.findall('\d+', str1)))
str1 = "12Prea20iapwoe68"
print("Sum of all the digits",find_sum(str1))

def FirstAndLast(string) :
    # Create an equivalent char array of the given string
    ch = list(string);
    i = 0 ;
    while i < len(ch):
        # k stores index of first character and i is going to store index of last character.
        k = i;
        while (i < len(ch) and ch[i] != ' ') :
            i += 1;
        # Check if the character is a small letter If yes, then Capitalise
        if (ord(ch[k]) >= 97 and
            ord(ch[k]) <= 122 ):
            ch[k] = chr(ord(ch[k]) - 32);
        else :
            ch[k] = ch[k]
        if (ord(ch[i - 1]) >= 90 and
            ord(ch[i - 1]) <= 122 ):
            ch[i - 1] = chr(ord(ch[i - 1]) - 32);
        else :
            ch[i - 1] = ch[i - 1]
        i += 1
    return "" . join(ch);
if __name__ == "__main__" :
    string = "Pro skim boarder";
    print("Input string "+string);
    print("String after Capitalize the first and last character of each word in a string:- "+FirstAndLast(string));

# Iterate on the input string
# For each character in string count and prints its frequency
# Use .count() method to do so.
string="yolo life"
for i in string:
    freq=string.count(i)
    print(str(i)+": "+str(freq),end=", ")

string="seventeen"
for i in string:
    count=0
    for j in string:
        if i==j:
            count+=1
        if count>1:
            break
    if count==1:
        print(i,end=" ")

String1="Listen"
String2="Silent"
String1=sorted(String1.lower())
String2=sorted(String2.lower())
if String1==String2:
    print('Anagrams')
else:
    print('Not')
#ALITER
from collections import Counter


def check(s1, s2):
    # printing counter
    print(Counter(s1))
    print(Counter(s2))
    if Counter(s1) == Counter(s2):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
s1 = "Listen"
s2 = "silent"
check(s1.lower(), s2.lower())

string=input("Enter String :\n")
str1=input("Enter substring which has to be replaced :\n")
str2=input("Enter substring with which str1 has to be replaced :\n")
string=string.replace(str1,str2)
print("String after replacement")
print(string)

#Count Common Subsequence in two Strings
n="ABC"
m="AB"
l1,l2=len(n),len(m)
cnt=[[0 for i in range(l2+1)] for i in range(l1+1)]
for i in range(1,l1+1):
    for j in range(1,l2+1):
         if(n[i-1] == m[j-1]):
             cnt[i][j] = 1 + cnt[i][j-1] + cnt[i-1][j]
         else:
             cnt[i][j] = cnt[i][j-1] + cnt[i-1][j] - cnt[i-1][j-1]
print(cnt[l1][l2])

def solve(a,b):
    n,m=len(a),len(b)
    if n==0 and m==0:
        return True
    if n > 1 and a[0] == '*' and m == 0:
        return False
    if (n > 1 and a[0] == '?') or (n != 0 and m !=0 and a[0] == b[0]):
        return solve(a[1:],b[1:]);
    if n !=0 and a[0] == '*':
        return solve(a[1:],b) or solve(a,b[1:])
    return False
str1="Prepins*a"
str2="Prepinsta"
print("First string with wild characters :" , str1)
print("Second string without wild characters ::" , str2)
print(solve(str1,str2))

#Lexicographic Permutations in Sorted Order
ans = []
def permute(a, l, r):
    if l == r:
        ans.append(''.join(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n)
for i in sorted(ans):
    print(i)
