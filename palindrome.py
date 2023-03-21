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
