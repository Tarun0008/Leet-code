class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ii=1
        o=1

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                o+=1
            else:
                o=1
            if o<=2:
                nums[ii]=nums[i]
                ii+=1
        return ii