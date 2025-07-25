class Solution:
    def maxSum(self, nums: List[int]) -> int:

        s=0
        ans=set(nums)
        for i in ans:
            if i >0:
                s+=i
        if s==0:
            return max(nums)
        return s