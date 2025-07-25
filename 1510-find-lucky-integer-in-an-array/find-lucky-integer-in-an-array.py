class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        ans=[]
        a=Counter(arr)
        res=-1
        print(a)
        for key,value in a.items():
            if key==value:
                res=max(res,key)
        return res
               