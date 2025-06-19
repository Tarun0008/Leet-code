class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_v=nums[0]
        ans=1
        for num in nums[1:]:
            if num-min_v >k:
                ans+=1
                min_v=num
        return ans
