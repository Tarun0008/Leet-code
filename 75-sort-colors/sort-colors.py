class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        
        l=0
        m=0
        h=len(nums)-1
        while(m<=h):
            
            if nums[m]==0:
                temp=nums[l]
                nums[l]=nums[m]
                nums[m]=temp
                m+=1
                l+=1
            elif nums[m]==1:
                m+=1
            elif nums[m]==2:
                temp=nums[h]
                nums[h]=nums[m]
                nums[m]=temp
                h-=1