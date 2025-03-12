class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p=0
        n=0
        for i in range(len(nums)):
            if nums[i]==0:
                pass
            elif nums[i]>0:
                p+=1
            else:
                n+=1
        res=max(p,n)
        print(res)
        return res       