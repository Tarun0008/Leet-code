class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        p=1
        for i in range(n):
            ans[i]=p
            p*=nums[i]
        s=1
        for i in range(n-1,-1,-1):
            ans[i]*=s
            s*=nums[i]
        return ans