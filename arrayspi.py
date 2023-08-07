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

def findDuplicate(arr):
    n = len(arr)
    duplicate = 0
    for currentNumber in range(1, n):
        count = 0
        for index in range(n):
            if (arr[index] == currentNumber) :
                count += 1            
        if (count > 1):
            duplicate = currentNumber
    return duplicate

def maxSubarrayProduct(arr,n):
    result=arr[0]
    for i in range(n):
        mul=arr[i]
        for j in range(i+1,n):
            result=max(result,mul)
            mul*=arr[j]
        result=max(result,mul)
    return result 
arr = [ 1, -2, -3, 0, 7, -8, -2 ]
n=len(arr)
print(maxSubarrayProduct(arr,n))

def areDis(set1,set2,m,n):
    set1.sort()
    set2.sort()
    #print(set1)
    #print(set2)
    i=0;j=0
    while(i<m and j<n):
        if(set1[i]<set2[j]):
            i+=1
        elif(set2[j]<set1[i]):
            j+=1
        else:
            return False
    return True
arr1 = [12, 34, 11, 9, 3]
arr2 = [7, 2, 1, 5]
m=len(arr1)
n=len(arr2)
print('Yes') if areDis(arr1,arr2,m,n) else print('No')

def areDis(set1,set2,n1,n2):
    myset=set([])
    # Traverse the first set and store its elements in hash
    for i in range(n1):
        myset.add(set1[i])
    for i in range(n2):
        if(set2[i] in myset):
            return False
    return True
arr1 = [10, 5, 3, 4, 6]
arr2 = [8, 7, 9, 3] 
n1 = len(arr1)
n2 = len(arr2)
if(areDis(arr1,arr2,n1,n2)):
    print('Yes')
else:
    print('nein')

'''It initializes two variables i and j to 0.
It iterates over each element of arr2 (outer loop) using the variable i.
For each element in arr2, it iterates over each element of arr1 (inner loop) using the variable j.
If the element in arr2 at index i is found in arr1 at index j, it breaks out of the inner loop and proceeds to the next element in arr2.
If the inner loop completes without finding the element from arr2 in arr1, it means arr2[i] is not present in arr1, and the function should return 0 (indicating that arr2 is not a subset of arr1).
If the outer loop completes without returning 0, it means all elements of arr2 are found in arr1, and the function should return 1 (indicating that arr2 is a subset of arr1).'''
def isSubset(arr1, arr2, m, n):
    for i in range(n):
        found = False
        for j in range(m):
            if arr2[i] == arr1[j]:
                found = True
                break
        if not found:
            return False
    return True
arr1 = [11, 12, 13, 21, 30, 70]
arr2 = [11, 30, 70, 12]
m = len(arr1)
n = len(arr2)
if isSubset(arr1, arr2, m, n):
    print("arr2[] is a subset of arr1[]")
else:
    print("arr2[] is not a subset of arr1[]")

def lcm(arr,length):
    for i in range(0,length):
        while arr[i]%2==0:
            arr[i]=arr[i]//2
        while arr[i]%3==0:
            arr[i]=arr[i]//3
    if arr[i]!=arr[0]:
        return False
    return True
arr = [50, 100, 75]
length=len(arr)
if lcm(arr,length):
    print("Yes, all the elements of the array can be made equal")
else:
    print("No can't be made equal")

def sumOfMinAbsDiff(arr,n):
    arr.sort()
    sum=0
    sum+=abs(arr[0]-arr[1]);
    sum+=abs(arr[n-1]-arr[n-2]);
    for i in range(1,n-1):
        sum+=min(abs(arr[i] - arr[i - 1]),
                  abs(arr[i] - arr[i + 1]))
    return sum;
arr = [2, 5, 4, 3]
n = len(arr)
print( "Required Sum =", sumOfMinAbsDiff(arr, n))

# hashing
from collections import Counter
def solve(arr1,arr2):
    res=[]
    f=Counter(arr1)
    for e in arr2:
        res.extend([e]*f[e])
        f[e]=0
    rem=list(sorted(filter(lambda x:f[x]!=0,f.keys())))
    for e in rem:
        res.extend([e]*f[e])
    return res
arr1 = [ 20, 1, 20, 5, 7, 1, 9, 39, 6, 18, 18 ];
arr2 = [ 20, 1, 18, 39 ];
print(*solve(arr1,arr2))

def changeArr(input1):
    newArray=input1.copy()
    newArray.sort()
    for i in range(len(input1)):
        for j in range(len(newArray)):
            if input1[i]==newArray[j]:
                input1[i]=j+1;
                break
arr=[100,2,75,30,90]
changeArr(arr)
print(arr)

a=[4,-2,0,6,-4]
ans=-1
for i in range(1,len(a)):
    if sum(a[:i])==sum(a[i+1:]):
        ans=i
        break
print('Equilibrium index of an array: ',ans)        

# Circular rotation of an array by K position
def circular_rotate_array(arr, K):
    # Calculate the effective value of K
    K = K % len(arr)
    # Reverse the entire array
    arr = arr[::-1]
    # Reverse the first K elements
    arr[:K] = arr[:K][::-1]
    # Reverse the remaining elements after Kth position
    arr[K:] = arr[K:][::-1]
    return arr
original_array = [1, 2, 3, 4, 5]
K = 2
result_array = circular_rotate_array(original_array, K)
print(result_array)  # Output: [4, 5, 1, 2, 3]
