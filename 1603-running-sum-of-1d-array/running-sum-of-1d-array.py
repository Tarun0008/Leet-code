class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        a=0
        for i in range(len(nums)):
            a+=nums[i]
            res.append(a)
        return res