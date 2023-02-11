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
