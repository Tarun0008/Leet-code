class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        f=float('inf')
        s=float('inf')        

        for num in nums:
            if num<=f:
                f=num
            elif num<=s:
                s=num
            else:
                return True
        return False