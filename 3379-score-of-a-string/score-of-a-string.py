class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=[]
        ss=0
        d=0
        for char in range(1,len(s)):
            d=abs(ord(s[char])-ord(s[char-1]))
            ss+=d
        print(ss)
        return ss