def get_word(sentence, n):
	# Only proceed if n is positive 
		sentence = sentence.split(" ")
		# Only proceed if n is not more than the number of words 
		if n <= len(sentence) and n>0:
			return(sentence[n-1])
		else:
			return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing
