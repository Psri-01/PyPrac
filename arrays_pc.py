class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum( [ (v-1)*v//2 for v in collections.Counter([ 10*min(i)+max(i) for i in dominoes ]).values() ]) 
''' step by step:
First we need to find a a way to assign a unique id to a domino regardless if it's [x:y] or [y:x]. Since domino value is 1<x<9, we can simply convert it into a 2 digit number like this [ 10*min(i)+max(i) for i in dominoes ] . Another approach would to use tuples like [ tuple(sorted(i)) for i in dominoes ].
Once we converted the original list of dominoes into a list of dominoes disregarding orientation, the next step is to calculate counts using collection.Counter(). It will produce a dictionary with values like 'domino1':count1, 'domino2':count2, ...
Since we just need the number of pairs, we can ignore the exact keys and just look at the values (the counts). Calculating pairs is a bit tricky, it's basically n*(n-1)//2 for each domino.
Finally we calculate the total count by using sum()'''

class Solution(object):
    def duplicateZeros(self, arr):
        i=0
        n=len(arr)
        while(i<n):
            if arr[i]==0:
                arr.pop()
                arr.insert(i,0)
                i+=1
            i+=1

from os import *
from sys import *
from collections import *
from math import *

def firstAndLastPosition(arr, n, k):
    first_last=[-1,-1]
    for i in range(n):
        if(arr[i]==k):
            if first_last[0]==-1:
                first_last[0]=i 
            first_last[1]=i
    return first_last

from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        counts = Counter(arr).values()
        return len(counts) == len(set(counts))

class Solution(object):
    def runningSum(self, nums):
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums

class Solution(object):
    def findDuplicates(self, nums):
        op=[]
        for num in nums:
            if nums[abs(num)-1]<0:
                op.append(abs(num))
            else:
                nums[abs(num)-1]*=-1
        return op

class Solution(object):
    def findDisappearedNumbers(self, nums):
        return set(range(1,len(nums)+1))-set(nums)

class Solution(object):
    def findDuplicates(self, nums):
        c=collections.Counter(nums)
        res=[]
        for k,v in c.items():
            if v==2:
                res.append(k)
        return res

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        start=0
        end=len(arr)-1
        mid=(start+end)//2
        while(start<end):
            if arr[mid]<arr[mid+1]:
                start=mid+1
            else:
                end=mid
            mid=(start+end)//2
        return start
