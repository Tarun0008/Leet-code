class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=sum(nums[:k])
        mx=window

        for i in range(k,len(nums)):
            window+=nums[i]-nums[i-k]
            mx=max(mx,window)
        return mx/k