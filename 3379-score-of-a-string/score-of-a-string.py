class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=[]
        ss=0
        d=0
        for char in s:
            ans.append(ord(char))
        for i in range(1,len(ans)):
            print(d)
            d=abs(ans[i]-ans[i-1])
            ss+=d
        print(ss)
        return ss