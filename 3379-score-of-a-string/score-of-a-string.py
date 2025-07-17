class Solution:
    def scoreOfString(self, s: str) -> int:
       
        ss=0
        for char in range(1,len(s)):
            ss+=abs(ord(s[char])-ord(s[char-1]))
        return ss