class Solution:
    def fp(self,val):

        if val:
            return 0
        else:
            return 1
    def minOperations(self, nums: List[int]) -> int:
        c=0
        for i in range((len(nums)-2)):
            if nums[i]==0:
                nums[i]=self.fp(nums[i])
                nums[i+1]=self.fp(nums[i+1])
                nums[i+2]=self.fp(nums[i+2])
                c=c+1
        return c if all(num == 1 for num in nums) else -1

        

        