class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx=0
        temp=0
        for i in range(len(nums)):
            if nums[i]==1:
                temp=temp+1
                print("temp",temp)
            else:
                print("max",maxx)
                print("temp2",temp)
                maxx=max(maxx,temp)

                temp=0
        return max(maxx,temp)