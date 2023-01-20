# Function to print three largest elements
import sys
#provides the name of the existing python modules which have been imported. 
#It function returns a list of command line arguments passed to a Python script.
def print3largest(arr, arr_size):
	# There should be atleast three elements
	if (arr_size < 3):
		print(" Invalid Input ")
		return
	third = first = second = -sys.maxsize
	for i in range(0, arr_size):
		# If current element is greater than first
		if (arr[i] > first):
			third = second
			second = first
			first = arr[i]
		# If arr[i] is in between first and second then update second
		elif (arr[i] > second):
			third = second
			second = arr[i]
		elif (arr[i] > third):
			third = arr[i]
	print("Three largest elements are", first, second, third)
# Driver program 
arr = [12, 13, 1, 10, 34, 1]
n = len(arr)
print3largest(arr, n)
