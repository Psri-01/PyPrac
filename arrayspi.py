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

