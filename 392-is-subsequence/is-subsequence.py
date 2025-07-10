class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c=0
        for char in t:
            if c<len(s) and s[c]==char:
                c=c+1
        return c==len(s)

        # c=0
        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         if s[i]==t[j]:
        #             c+=1
        #             print(c,s[i])
        #             if c==len(s):
        #                 return True
        #         else:
        #             i=i+1
        # return False