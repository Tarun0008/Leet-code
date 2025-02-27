class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapp={}
        for i,n in enumerate(nums):
            d=target-n
            if d in mapp:
                return [mapp[d],i]
            else:
                mapp[n]=i
        