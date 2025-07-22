class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen=set()
        l=0
        cs=0
        ms=0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[l])
                cs-=nums[l]
                l+=1
            seen.add(nums[right])
            cs+=nums[right]
            ms=max(cs,ms)
        return ms