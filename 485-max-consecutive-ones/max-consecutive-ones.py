class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx=0
        temp=0
        for i in range(len(nums)):
            if nums[i]==1:
                temp=temp+1
            else:
                maxx=max(maxx,temp)
                temp=0
        return max(maxx,temp)