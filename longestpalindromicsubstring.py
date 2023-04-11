class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp=''
        for i in range(len(s)):
            temp=max(temp,expand(s,i,i), expand(s,i,i+1), key=len)
        return temp
            
def expand(s,i,j):
    while i>=0 and j<len(s) and s[i]==s[j]:
        i-=1
        j+=1
    return s[i+1:j]
