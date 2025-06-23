class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wsum=sum(nums[:k])
        maxs=wsum

        for i in range(k,len(nums)):
            wsum=wsum-nums[i-k]+nums[i]
            maxs=max(maxs,wsum)
        return maxs/k
        