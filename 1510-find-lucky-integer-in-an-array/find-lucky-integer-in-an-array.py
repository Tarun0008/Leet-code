class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        ans=[]
        a=Counter(arr)
        a.most_common()
        print(a)
        for key,value in a.items():
            if key==value:
                ans.append(key)
            
        return max(ans) if ans else -1