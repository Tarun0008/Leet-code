class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        a=list(s)
        z=0
        for i in range(len(indices)):
            res[indices[i]]=a[i] 
            print(res)
        return "".join(res)