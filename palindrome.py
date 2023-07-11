def is_palindrome(input_string):
	new_string = ""
	reverse_string = ""
	for letter in input_string:
		if letter != " ":
			new_string += letter.lower() 
			reverse_string = letter.lower() + reverse_string
	if new_string == reverse_string:
		return reverse_string + " is a palindrome"
	return reverse_string + " is not a palindrome"		    
print(is_palindrome("applppe"))
print(is_palindrome("malayalam"))

#ITERATION
num=1234321
temp=num
reverse=0
while temp>0:
    remainder=temp%10
    reverse=(reverse*10)+remainder
    temp=temp//10
if num==reverse:
    print('Palindrome')
else:
    print('Not Palindrome')

#SLICING
num=12321
rev=int(str(num)[::-1])
if num==rev:
    print('Palindrome')
else:
    print('Not a Palindrome')

#RECURSION
def recurrev(num,rev):
    if num==0:
        return rev
    remainder=int(num%10)
    rev=(rev*10)+remainder
    return recurrev(int(num/10),rev)
num=1234321
rev=0 
rev=recurrev(num,rev)
print(str(num)+" is a ",end="")
print('Palindrome') if rev==num else print('Not Palindrome')

#STRIN MATCHING
def checkPalindrome(str):
    for i in range(0,len(str)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
s="kayak"
print('Palindrome') if checkPalindrome(s) else print('Not Palindrome')

#ALITER
return str(x)[::-1] == str(x)

#ALITER
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        orig = x
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10
        return rev == orig

#ALITER
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        half = 0
        while x > half:
            half = (half * 10) + (x % 10)
            x = x // 10
        return x == half or x == half // 10
