class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans=0
        s=0

        for num in nums:
            if num==0:
                s+=1
                ans+=s
            else:
                s=0
        return ans