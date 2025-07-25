class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        
        a=Counter(arr)
        res=-1
        for key,value in a.items():
            if key==value:
                res=max(res,key)
        return res
               