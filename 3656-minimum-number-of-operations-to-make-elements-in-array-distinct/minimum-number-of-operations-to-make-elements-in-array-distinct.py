class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        see=set()
        a=0
        i=0


        while len(nums)>0:
            c=nums[i:]
            if len(set(c))==len(c):
                break
            i=i+3
            a+=1
        return a