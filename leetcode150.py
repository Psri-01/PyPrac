# happy number
class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(7):
            n = sum([int(i)**2 for i in str(n)])
        return n == 1        
# merge sorted array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1.remove(0)
            nums1.append(nums2[i])
        nums1.sort()
# climbing stairs
'''class Solution {
public:
    int climbStairs(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        int prev = 1, curr = 1;
        for (int i = 2; i <= n; i++) {
            int temp = curr;
            curr = prev + curr;
            prev = temp;
        }
        return curr;
    }
};'''
#py
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
# pali
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)
# plus1
class Solution(object):
    def plusOne(self, digits):
        s = "".join(str(x) for x in digits)
        s = str(int(s) + 1)
        return [int(x) for x in s]
# single number
class Solution(object):
    def singleNumber(self, nums):
        return 2*sum(set(nums)) - sum(nums)
# merge 2 sorted link lists - c++
# valid parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        para = dict(("{}","()","[]"))
        stack = []
        for idx in s:
            if idx in '{([':
                stack.append(idx)
            elif len(stack)==0 or idx!=para[stack.pop()]:
                return False
        return len(stack)==0
# remove elem from integer array
class Solution(object):
    def removeElement(self, nums, val):
        idx=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[idx]=nums[i]
                idx+=1
        return idx
# remove duplicates from sorted array
class Solution(object):
    def removeDuplicates(self, nums):
        np=defaultdict(int)
        ans=[]
        x=0
        for i in nums:
            np[i]+=1
            if np[i]==1:
                nums[x]=i
                x+=1
        return len(np)
# best time to buy and sell stock
'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''
class Solution(object):
    def maxProfit(self, prices):
        profit=0
        buy=prices[0]
        for x in prices[1:]:
            buy=min(buy,x)
            profit=max(profit,x-buy)
        return profit
