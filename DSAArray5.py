# Quicksort with avg. case Time complexity = O(nLogn)
def find3largest(arr, n):
	arr = sorted(arr) 
	check = 0
	count = 1
	for i in range(1, n + 1):
		if(count < 4):
			if(check != arr[n - i]):
				# to handle duplicate values
				print(arr[n - i], end = " ")
				check = arr[n - i]
				count += 1
		else:
			break
# Driver code
arr = [12, 45, 1, -1, 45,	54, 23, 5, 0, -10]
n = len(arr)
find3largest(arr, n)
