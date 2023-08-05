a=[10,89,95,1,6,38,80]
max_elem=a[0]
for i in range(len(a)):
    if a[i]>max_elem:
        max_elem=a[i]
print(max_elem)

arr = [10, 19, 59, 6, 3, 80, 98]
mini = arr[0]
for i in range(len(arr)):
    if arr[i]<mini:
        mini=arr[i]
print(mini)

arr = [10, 89, 9, 56, 4, 80, 8]
mini = arr[0]
maxi = arr[0]
for i in range(len(arr)):
  if arr[i] < mini: mini = arr[i] 
if arr[i] > maxi: maxi = arr[i]
print (mini)
print (maxi)
#ALITER
arr = [10, 89, 9, 56, 4, 80, 8]
arr.sort()
print (arr[0])
print (arr[-1])

import math
arr = [10, 13, 17, 11, 34, 21]
arr.sort();
print(arr[1])

arr = [10, 13, 17, 11, 34, 21]
sum=0
for i in range(len(arr)):
    sum=sum+arr[i]
print(sum)

def reverseList(A,start,end):
    while start<end:
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1
A=[10,20,30,40,50]
reverseList(A,0,4)
print(A)

# sort first half in ascending order second half in descending order
def printOrder(arr,n):
    arr.sort()
    i=0
    while (i<n/2):
        print (arr[i],end=" ")
        i=i+1
    j=n-1
    while j>=n/2:
        print (arr[j],end=" ")
        j=j-1
arr=[1,90,34,29,89,7,20]
n=len(arr)
printOrder(arr,n)

arr=[1,100,813,90,34,29,69,7,20]
arr.sort()
print(arr)
arr=[1,100,813,90,34,29,69,7,20]
arr.sort(reverse=True)
print(arr)

'''Declare a dictionary dict().
Start iterating over the entire array
If element is present in map, then increase the value of frequency by 1.
Otherwise, insert that element in map.
After complete iteration over array, start traversing map and print the key-value pair.''''
def countFreq(arr,n):
    mp=dict()
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    for x in mp:
        print(x," ",mp[x])
arr = [10, 30, 10, 20, 10, 20, 30, 10] 
n=len(arr)
countFreq(arr,n)
#ALITER
def countdist(arr,n):
    arr.sort()
    # traverse the sorted array
    i=0
    while i<n:
        count=1
        # Move the index ahead whenever you encounter  duplicates
        while i<n-1 and arr[i]==arr[i+1]:
            i+=1
            count+=1
        print("{0}: {1}".format(arr[i], count))
        i+=1
arr = [5,0,5,9,5,7,9,7,7,10]
n = len(arr)
countdist(arr, n)

# Sorting elements of an Array by Frequency
from collections import Counter
ini_list=[10,20,30,40,40,50,50,50]
result=[item for items,c in Counter(ini_list).most_common() for item in [items]*c]
print(str(result))

#Largest palindrome in an array
def largestPalindrome(arr):
    pal=-1
    for i in arr:
        if str(i)==str(i)[::-1]:
            if i>pal:
                pal=i
        else:
            pass
    return pal
arr = [1, 232, 54545, 999991, 8813200023188]
print(largestPalindrome(arr))

#count of distinct elems in an array
def count(arr,n):
    mp=dict()
    count_dis=0
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    print(len(mp))
arr = [10, 30, 40, 20, 10, 20, 50, 10] 
n = len(arr) 
count(arr, n)
# repeating
def count(arr,n):
    mp=dict()
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    for x in mp:
        if mp[x]!=1:
            print(x, end=" ")
arr = [10, 30, 40, 20, 10, 20, 50, 10] 
n = len(arr) 
count(arr, n)
# non rep
def count(arr,n):
    mp=dict()
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    for x in mp:
        if mp[x]==1:
            print(x, end=" ")
arr = [10, 30, 40, 20, 10, 20, 50, 10] 
n = len(arr) 
count(arr, n)

def removeDuplicates(arr, n):
# Return, if array is empty or contains a single element
    if n == 0 or n == 1:
        return n
    temp = list(range(n))
    # Start traversing elements
    j = 0;
    for i in range(0, n-1):
        # If current element is not equal to next element then store that current element
        if arr[i] != arr[i+1]:
            temp[j] = arr[i]
            j += 1
    temp[j] = arr[n-1]
    j += 1
    # Modify original array
    for i in range(0, j):
        arr[i] = temp[i]
    return j
arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]
n = len(arr)

n = removeDuplicates(arr, n)
# Print updated array
for i in range(n):
    print ("%d"%(arr[i]), end = " ")

arr1 = [1, 2, 6, 3, 7]
arr2 = [10, 7, 45, 3, 7]
n=len(arr1)
arr1.sort()
arr2.sort(reverse=True)
product=0
for i in range(n):
    product+=arr1[i]*arr2[i]
print(product, end)

arr1 = [1, 2, 6, 3, 7]
arr2 = [10, 7, 45, 3, 7]
n=len(arr1)
arr1.sort()
arr2.sort()
product=0
for i in range(n):
    product+=arr1[i]*arr2[i]
print(product, end)

arr = [1, 7, 8, 4, 5, 16, 8]
n=len(arr)
countEven=0
countOdd=0
for i in range(0,n):
    if arr[i]%2==0:    #or if arr[i]&1==0
        countEven+=1
    else:
        countOdd+=1
print('Even elems count: ',countEven)
print('Odd elems count: ',countOdd)

# Symmetric pairs in arrays
def findPairs(pairs):
    s=set()
    for (x,y) in pairs:
        s.add((x,y))
        if (y,x) in s:
            print((x,y))
pairs = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
findPairs(pairs)
