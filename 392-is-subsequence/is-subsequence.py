class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c=0
        for char in t:
            if c<len(s) and s[c]==char:
                c=c+1
        return c==len(s)
