class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            a.append(s.index(i))
            
        for i in t:
            b.append(t.index(i))
            
        if a!=b :
            return False
       
        return True