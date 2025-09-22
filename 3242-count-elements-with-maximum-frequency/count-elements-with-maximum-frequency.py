class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=Counter(nums)
        ans=0
        m=max(freq.values())
        for k in freq.values():
            if k==m:
                ans+=k
        return ans