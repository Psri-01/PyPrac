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
