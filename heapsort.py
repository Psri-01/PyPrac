# To heapify subtree rooted at index i.
# n is size of heapdef heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
# See if left child of root exists and is# greater than rootif l < n and arr[i] < arr[l]:
        largest = l
    # See if right child of root exists and is greater than rootif r < n and arr[largest] < arr[r]:
        largest = r
        arr[i],arr[largest] = arr[largest],arr[i]  # swap, Heapify the root.
        heapify(arr, n, largest)
    n = len(arr)
        heapify(arr, n, i)
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i])
