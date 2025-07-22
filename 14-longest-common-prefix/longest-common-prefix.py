class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        p=0
        s=strs[0]
        while p<=len(s) and all(a.startswith(s[:p+1]) for a in strs):
            p+=1
        return s[:p]