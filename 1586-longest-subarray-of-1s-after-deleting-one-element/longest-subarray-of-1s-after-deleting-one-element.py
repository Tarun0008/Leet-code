class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        c=0
        l=0
        a=0
        z=0
        for right in range(len(nums)):
            if nums[right]==0:
                z+=1
            
            while z>1:
                if nums[l]==0:
                    z-=1
                l+=1
            a=max(a,right-l+1-z)
        return a-1 if a==len(nums) else a