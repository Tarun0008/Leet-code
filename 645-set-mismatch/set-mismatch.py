class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=set()
        d=0

        for num in nums:
            if num in res:
                d=num
            res.add(num)
        
        s=sum(res)
        b=n*(n+1)//2
        ans=b-s
        return[d,ans]
        