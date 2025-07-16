class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        last={}

        for i,num in enumerate(nums):
            if num in last:
                if i-last[num]<=k:
                    return True
            last[num]=i

        return False
        
    
    
    
    
    
    
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j] and abs(i-j)<=k:
        #             return True
        # return False