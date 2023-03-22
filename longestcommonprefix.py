class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the list is empty, return an empty string
        if not strs:
            return ""
        
        # Find the length of the shortest string in the list
        min_len = min(len(s) for s in strs)
        
        # Iterate through the characters in the shortest string
        for i in range(min_len):
            # Check if the character at the i-th position is the same for all strings
            if not all(s[i] == strs[0][i] for s in strs):
                # If not, return the longest common prefix found so far
                return strs[0][:i]
        
        # If all characters are the same for all strings, return the shortest string
        return strs[0][:min_len]
